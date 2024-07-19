import Vue from 'vue'  
import Router from 'vue-router'  
import Login from '../components/LoginPage.vue'  
import HospitalUsers from '../components/HospitalUsers.vue'  
import HospitalList from '../components/HospitalList.vue'  
import HospitalDashboard from '../components/HospitalDashboard.vue'  
import HospitalTraffic from '../components/HospitalTraffic.vue'  
import GovernanceDetails from '../components/GovernanceDetails.vue'  
import GovernanceEdit from '../components/GovernanceEdit.vue'  
  
Vue.use(Router)  
  
export default new Router({  
  mode: 'history', // 使用 HTML5 History 模式  
  routes: [  
    {  
      path: '/',  
      redirect: '/login' // 默认重定向到登录页面  
    },  
    {  
      path: '/login',  
      name: 'Login',  
      component: Login  
    },  
    {  
      path: '/hospital-users',  
      name: 'HospitalUsers',  
      component: HospitalUsers  
    },  
    {  
      path: '/hospital-list',  
      name: 'HospitalList',  
      component: HospitalList  
    },  
    {  
      path: '/hospital-dashboard',  
      name: 'HospitalDashboard',  
      component: HospitalDashboard  
    },  
    {  
      path: '/hospital-traffic',  
      name: 'HospitalTraffic',  
      component: HospitalTraffic  
    },  
    {  
      path: '/governance-details',  
      name: 'GovernanceDetails',  
      component: GovernanceDetails  
    },  
    {  
      path: '/governance-edit',  
      name: 'GovernanceEdit',  
      component: GovernanceEdit  
    }  
  ]  
})