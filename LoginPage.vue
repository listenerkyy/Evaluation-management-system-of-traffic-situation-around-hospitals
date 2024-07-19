<template>  
  <div class="container mt-5">  
    <div class="row justify-content-center">  
      <div class="col-md-6">  
        <div class="card">  
          <div class="card-header">  
            <h3 class="text-center">医院周边交通治理评价管理系统</h3>  
          </div>  
          <div class="card-body">  
            <form @submit.prevent="handleLogin">  
              <div class="mb-3">  
                <label for="username" class="form-label">账号</label>  
                <input type="text" class="form-control" id="username" v-model="loginForm.username" required>  
              </div>  
              <div class="mb-3">  
                <label for="password" class="form-label">密码</label>  
                <input type="password" class="form-control" id="password" v-model="loginForm.password" required>  
              </div>  
              <button type="submit" class="btn btn-primary btn-block">登录</button>  
            </form>  
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
      loginForm: {  
        username: '',  
        password: ''  
      }  
    }  
  },  
  methods: {  
    handleLogin() {  
      // 这里可以添加登录逻辑，比如API调用  
      console.log('登录信息:', this.loginForm);  
      // 模拟登录成功  
      alert('登录成功！');  
    }  
  }  
}  
</script>  
  
<style scoped>  
/* 在这里添加CSS样式 */  
</style>