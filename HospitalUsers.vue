<template>  
  <div class="container mt-5">  
    <h1 class="mb-4">医院周边交通治理评价管理系统</h1>  
    <nav class="nav nav-tabs">  
      <router-link to="/home" class="nav-item nav-link active" aria-current="page">首页</router-link>  
      <router-link to="/user-management" class="nav-item nav-link">用户管理</router-link>  
      <!-- 其他选项卡链接 -->  
    </nav>  
    <div class="card mt-4">  
      <div class="card-header">  
        用户管理  
      </div>  
      <div class="card-body">  
        <table class="table table-striped">  
          <thead>  
            <tr>  
              <th>#</th>  
              <th>用户名</th>  
              <th>用户名称</th>  
              <th>用户性别</th>  
              <th>用户类型</th>  
              <th>联系方式</th>  
              <th>操作</th>  
            </tr>  
          </thead>  
          <tbody>  
            <tr v-for="(user, index) in users" :key="index">  
              <td>{{ index + 1 }}</td>  
              <td>{{ user.username }}</td>  
              <td>{{ user.name }}</td>  
              <td>{{ user.gender }}</td>  
              <td>{{ user.type }}</td>  
              <td>{{ user.contact }}</td>  
              <td>  
                <!-- 这里可以添加编辑、删除等操作按钮 -->  
                <button class="btn btn-primary btn-sm">编辑</button>  
                <button class="btn btn-danger btn-sm">删除</button>  
              </td>  
            </tr>  
          </tbody>  
        </table>  
      </div>  
    </div>  
  </div>  
</template>  
  
<script setup>  
import { ref } from 'vue';  
  
const users = ref([  
  { username: 'user1', name: '张三', gender: '男', type: '管理员', contact: '12345678901' },  
  { username: 'user2', name: '李四', gender: '女', type: '普通用户', contact: '09876543210' },  
  // 更多用户数据...  
]);  
</script>  
  
<style scoped>  
/* 这里可以添加一些特定于这个组件的样式 */  
</style>