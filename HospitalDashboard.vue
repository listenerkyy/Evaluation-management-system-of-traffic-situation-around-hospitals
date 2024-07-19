<template>  
  <div class="container mt-5">  
    <!-- 导航栏 -->  
    <nav class="navbar navbar-expand-lg navbar-light bg-light">  
      <a class="navbar-brand" href="#">医院周边交通治理评价管理系统</a>  
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">  
        <span class="navbar-toggler-icon"></span>  
      </button>  
      <div class="collapse navbar-collapse" id="navbarNav">  
        <ul class="navbar-nav">  
          <li class="nav-item">  
            <router-link to="/" class="nav-link active" aria-current="page">首页</router-link>  
          </li>  
          <li class="nav-item">  
            <router-link to="/user-management" class="nav-link">用户管理</router-link>  
          </li>  
          <!-- 其他导航项 -->  
        </ul>  
      </div>  
    </nav>  
  
    <!-- 医院列表 -->  
    <div class="mt-4">  
      <h2>医院列表</h2>  
      <div class="list-group">  
        <a href="#" class="list-group-item list-group-item-action flex-column align-items-start" v-for="hospital in hospitals" :key="hospital.id">  
          <div class="d-flex w-100 justify-content-between">  
            <h5 class="mb-1">{{ hospital.name }}</h5>  
            <small>{{ hospital.location }}</small>  
          </div>  
          <p class="mb-1">{{ hospital.date }}</p>  
          <small class="text-muted">{{ hospital.score }} 分</small>  
          <div class="d-flex w-100 justify-content-between">  
            <button class="btn btn-primary btn-sm me-2">查看详情</button>  
            <button class="btn btn-secondary btn-sm">编辑</button>  
          </div>  
        </a>  
      </div>  
    </div>  
  </div>  
</template>  
  
<script setup>  
import { ref } from 'vue';  
  
const hospitals = ref([  
  { id: 1, name: '北京积水潭医院', location: '西城区', date: '2024-07-16', score: 45 },  
  { id: 2, name: '北京大学人民医院', location: '西城区', date: '2024-07-16', score: 34 },  
  // 更多医院数据...  
]);  
</script>  
  
<style scoped>  
/* 这里可以添加一些特定于这个组件的样式 */  
</style>