<template>
    <el-table v-loading="loading" :data="userData" stripe style="width: 100%">
        <el-table-column prop="username" label="姓名" width="180" />
        <el-table-column prop="postname" label="岗位" width="180" />
        <el-table-column prop="date" label="日期" />
    </el-table>
    <el-pagination :page-size="page_size" :page-count="pages" :pager-count="7" :page-sizes="[1, 2, 3, 4]"
        layout="prev, pager, next, sizes" :hide-on-single-page="true" v-model:currentPage="current_page"
        @update:current-page="getUser" @update:page-size="handlePageSize" />
</template>

<script lang="ts" setup>
import { ref } from 'vue';
import { getUserByPage } from '@/api'
import { useRoute } from 'vue-router'

let current_page = ref(1)
let page_size = ref(1)
let pages = ref(1)
let loading = ref(true)

let userData = ref([])

const getUser = () => {
    loading.value = true
    let dd = getUserByPage(current_page.value, page_size.value)
    dd.then((data) => {
        pages.value = data.data.pages
        userData.value = data.data.data
        loading.value = false
    })
}

const handlePageSize = (size) => {
    page_size.value = size
    getUser()
}
getUser()
</script>