<template>  
  <div class="container mt-5">  
    <h2 class="text-center">医院周边交通治理评价管理系统</h2>  
    <div class="row justify-content-center mt-4">  
      <div class="col-md-8">  
        <nav class="nav nav-tabs">  
          <a class="nav-item nav-link active" href="#">用户管理</a>  
          <a class="nav-item nav-link" href="#">医院信息管理</a>  
          <a class="nav-item nav-link" href="#">卫健委综合治理</a>  
        </nav>  
        <div class="card mt-3">  
          <div class="card-header">  
            医院列表  
          </div>  
          <div class="card-body">  
            <table class="table table-striped">  
              <thead>  
                <tr>  
                  <th>序号</th>  
                  <th>医院名称</th>  
                  <th>医院区属</th>  
                  <th>医院类型</th>  
                  <th>操作</th>  
                </tr>  
              </thead>  
              <tbody>  
                <tr v-for="(hospital, index) in hospitals" :key="index">  
                  <td>{{ index + 1 }}</td>  
                  <td>{{ hospital.name }}</td>  
                  <td>{{ hospital.district }}</td>  
                  <td>{{ hospital.type }}</td>  
                  <td>  
                    <button class="btn btn-primary btn-sm">编辑</button>  
                    <button class="btn btn-danger btn-sm" @click="deleteHospital(index)">删除</button>  
                  </td>  
                </tr>  
              </tbody>  
            </table>  
            <nav aria-label="Page navigation example">  
              <ul class="pagination">  
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>  
                <li class="page-item"><a class="page-link" href="#">1</a></li>  
                <li class="page-item"><a class="page-link" href="#">2</a></li>  
                <li class="page-item"><a class="page-link" href="#">3</a></li>  
                <li class="page-item"><a class="page-link" href="#">Next</a></li>  
              </ul>  
            </nav>  
          </div>  
        </div>  
      </div>  
    </div>  
  </div>  
</template>  
  
<script>  
export default {  
  data() {  
    return {  
      hospitals: [  
        { name: '医院A', district: '区A', type: '综合医院' },  
        { name: '医院B', district: '区B', type: '专科医院' },  
        // 更多医院数据...  
      ],  
    };  
  },  
  methods: {  
    deleteHospital(index) {  
      // 实现删除逻辑，这里只是示例  
      this.hospitals.splice(index, 1);  
    },  
  },  
};  
</script>  
  
<style scoped>  
/* 在这里添加你的CSS样式 */  
</style>