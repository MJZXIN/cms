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
    <el-table-column prop="uid" label="岗位编号" width="80" />
    <el-table-column prop="postcode" label="岗位编码" width="100" />
    <el-table-column prop="postname" label="岗位名称" width="160" />
    <el-table-column label="状态" width="60">
      <template #default="scope">
        <el-tag v-if="scope.status">禁用</el-tag>
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
    title="新建岗位"
    width="60%"
    :before-close="handleClose"
  >
    <el-form :model="form">
      <el-form-item label="岗位名称">
        <el-input v-model="formData.postname" /> </el-form-item
      ><el-form-item label="岗位编码">
        <el-input v-model="formData.postcode" />
      </el-form-item>
      <el-form-item label="岗位状态">
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
import { getPost, addPost } from "api/system";
import { ElMessage } from "element-plus";

export default {
  data() {
    return {
      tableData: [],
      total_page: 1,
      loading: false,
      dialogVisible: false,
      formData: {
        postname: "",
        postcode: "",
        status: "1",
      },
    };
  },
  methods: {
    handleCurrentChange(page) {
      this.loading = true;
      getPost(page)
        .then((res) => {
          this.tableData = res.data.data_list;
          this.total_page = res.data.total_page;
          this.loading = false;
        })
        .catch(() => {
          this.loading = false;
        });
    },
    handleAdd() {
      addPost(this.formData)
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
