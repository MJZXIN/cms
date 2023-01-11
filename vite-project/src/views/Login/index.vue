<template>
    <div>Login</div>
    <button @click="getTestFrom">测试</button>
</template>

<script setup>
import { getTest } from '../../api'

function getTestFrom() {
    console.log("按下")
    getTest().then((res)=> {
        console.log(res.data)
    })
}
</script>