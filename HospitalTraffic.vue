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
          <li class="nav-item active">  
            <a class="nav-link" aria-current="page" href="#">首页</a>  
          </li>  
          <li class="nav-item">  
            <a class="nav-link" href="#">用户管理</a>  
          </li>  
          <li class="nav-item">  
            <a class="nav-link" href="#">医院信息管理</a>  
          </li>  
          <!-- 添加其他导航项 -->  
        </ul>  
      </div>  
    </nav>  
  
    <!-- 医院列表 -->  
    <div class="mt-4">  
      <h2>医院交通治理评价</h2>  
      <div class="table-responsive">  
        <table class="table table-striped">  
          <thead>  
            <tr>  
              <th>医院名称</th>  
              <th>时间</th>  
              <th>日期</th>  
              <th>分数</th>  
              <th>操作</th>  
            </tr>  
          </thead>  
          <tbody>  
            <tr v-for="hospital in hospitals" :key="hospital.id">  
              <td>{{ hospital.name }}</td>  
              <td>{{ hospital.year }}</td>  
              <td>{{ hospital.date }}</td>  
              <td>{{ hospital.score }}</td>  
              <td>  
                <button class="btn btn-primary btn-sm">查看详情</button>  
                <button class="btn btn-secondary btn-sm">编辑</button>  
                <button class="btn btn-danger btn-sm">删除</button>  
              </td>  
            </tr>  
            <!-- 如果需要分页，可以在这里添加分页逻辑 -->  
          </tbody>  
        </table>  
      </div>  
      <!-- 如果需要显示记录总数，可以添加以下行 -->  
      <div class="mt-3">  
        <p>共 {{ hospitals.length }} 条记录</p>  
      </div>  
    </div>  
  </div>  
</template>  
  
<script setup>  
import { ref } from 'vue';  
  
// 模拟的医院数据  
const hospitals = ref([  
  { id: 1, name: '北京积水潭医院', year: '2024-01', date: '2024/7/16', score: 45 },  
  { id: 2, name: '北京大学人民医院', year: '2024-12', date: '2024/7/16', score: 34 },  
  // 更多医院数据...  
]);  
</script>  
  
<style scoped>  
/* 在这里添加组件的样式 */  
</style>