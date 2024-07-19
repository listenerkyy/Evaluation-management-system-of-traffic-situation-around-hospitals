<template>  
  <div class="governance-details">  
    <h1>卫健委综合治理情况详情</h1>  
    <div class="detail-info">  
      <p><strong>医院名称:</strong> {{ hospital.name }}</p>  
      <p><strong>医院区属:</strong> {{ hospital.district }}</p>  
      <p><strong>日期:</strong> {{ hospital.date }}</p>  
      <p><strong>上下午门诊号源比例:</strong> {{ hospital.morningAfternoonRatio }}</p>  
      <p><strong>预约就诊比例:</strong> {{ hospital.reservationRate }}%</p>  
      <p><strong>预约就诊精准时间:</strong> {{ hospital.reservationAccuracy }}分钟</p>  
      <p><strong>医院内停车位开放比例:</strong> {{ hospital.parkingRate }}%</p>  
      <p><strong>ETC收费智能系统:</strong> {{ hospital.etcSystem ? '启用' : '未启用' }}</p>  
      <p><strong>禁停标志标线:</strong> {{ hospital.noParkingSigns ? '有' : '无' }}</p>  
      <p><strong>行人过街设施:</strong> {{ hospital.crosswalkFacilities }}</p>  
      <p><strong>限速或减速标志标识:</strong> {{ hospital.speedLimitSigns ? '开启' : '关闭' }}</p>  
      <!-- 根据需要添加更多字段 -->  
    </div>  
  </div>  
</template>  
  
<script>  
export default {  
  data() {  
    return {  
      hospital: {  
        name: '北京积水潭医院',  
        district: '西城区',  
        date: '2024/7/16',  
        morningAfternoonRatio: '1.2:1',  
        reservationRate: 100,  
        reservationAccuracy: 30,  
        parkingRate: 95,  
        etcSystem: true,  
        noParkingSigns: true,  
        crosswalkFacilities: '完善',  
        speedLimitSigns: false,  
        // 根据需要添加更多数据  
      },  
    };  
  },  
};  
</script>  
  
<style scoped>  
/* 样式代码 */  
</style>