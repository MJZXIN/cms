<template>
  <div class="button-span">
    <el-button type="primary" @click="dialogVisible = true">新建</el-button>
    <el-button type="success">Success</el-button>
    <el-button type="info">Info</el-button>
    <el-button type="warning">Warning</el-button>
    <el-button type="danger">Danger</el-button>
  </div>
  <el-table
    v-loading="loading"
    row-key="uid"
    lazy
    :load="load"
    :data="tableData"
    style="width: 100%"
  >
    <el-table-column prop="uid" label="产品编号" width="80" />
    <el-table-column prop="prodname" label="产品名称" width="160" />
    <el-table-column prop="prod_spec" label="产品规格" width="160" />
    <el-table-column prop="whshname" label="产品位置" width="80" />
    <el-table-column prop="prod_cost" label="产品价格" width="80" />
    <el-table-column prop="prod_brand" label="品牌" width="80" />
    <el-table-column label="状态" width="60">
      <template #default="scope">
        <el-tag v-if="scope.status">缺货</el-tag>
        <el-tag v-else>正常</el-tag>
      </template>
    </el-table-column>
    <el-table-column prop="create_by" label="创建者" width="120" />
    <el-table-column fixed="right" label="操作">
      <template #default>
        <el-button link type="primary" size="small" @click="handleClick"
          >详情</el-button
        >
        <el-button link type="primary" size="small">编辑</el-button>
        <el-button link type="primary" size="small">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <el-pagination
    layout="prev, pager, next"
    :total="10"
    :page-count="total_page"
    :small="false"
    :background="false"
    :hide-on-single-page="true"
    @current-change="handleCurrentChange"
  />

  <el-dialog
    v-model="dialogVisible"
    title="新建零件"
    width="60%"
    :before-close="handleClose"
  >
    <el-form :model="form">
      <el-form-item label="产品名称">
        <el-input v-model="formData.partname" /> </el-form-item
      ><el-form-item label="产品规格">
        <el-input v-model="formData.part_spec" />
      </el-form-item>
      <el-form-item label="产品位置">
        <el-cascader
          v-model="formData.whshname"
          :options="whshList"
          :show-all-levels="true"
        />
      </el-form-item>
      <el-form-item label="产品数量">
        <el-input type="number" min="0" v-model="formData.total_number" />
      </el-form-item>
      <el-form-item label="产品价格">
        <el-input type="number" min="0" v-model="formData.part_cost" />
      </el-form-item>
      <el-form-item label="状态">
        <el-radio-group v-model="formData.status">
          <el-radio label="1">正常</el-radio>
          <el-radio label="0">停用</el-radio>
        </el-radio-group>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="handleAdd">添加</el-button>
        <el-button @click="dialogVisible = false">取消</el-button>
      </span>
    </template>
  </el-dialog>
</template>

<script>
import { getProduct, addProduct } from "api/product";
import { ElMessage } from "element-plus";

export default {
  data() {
    return {
      tableData: [],
      total_page: 1,
      loading: false,
      dialogVisible: false,
      whshList: [],
      formData: {
        partname: "",
        part_spec: "",
        part_type: "原材料",
        whshname: "",
        total_number: 0,
        part_cost: 0.0,
        status: "1",
      },
    };
  },
  methods: {
    handleCurrentChange(page) {
      this.loading = true;
      getProduct(page)
        .then((res) => {
          this.tableData = res.data.data_list;
          this.total_page = res.data.total_page;
          this.whshList = res.data.whsh_list;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
    handleAdd() {
      addPart(this.formData)
        .then((res) => {
          ElMessage(res.msg);
          this.dialogVisible = false;
        })
        .catch((res) => {
          ElMessage({
            message: res.msg,
            type: "warning",
          });
        });
    },
  },
  created() {
    this.handleCurrentChange(1);
  },
};
</script>

<style>
.button-span {
  display: flex;
  margin-bottom: 10px;
}
</style>
