
<template>
<div>
  <div id="nav-bar">
    <div id="container">
      <div class="nav-brand-item"></div>
      <div class="user-account" ><i class="el-icon-user-solid"><span style="margin-left: 5px">Account</span></i></div>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" id="nav"
               text-color="#8f9397"
               active-text-color="#4cbd89"
      >
      <el-menu-item index="1">Fuel Quote</el-menu-item>
      <el-menu-item index="2">Fuel Quote History</el-menu-item>
      </el-menu>
      <!--<div class="line"></div>-->

    </div>

  </div>
  <div class="main-container">
    <transition name="fade-transform" mode="out-in">
     <div v-if="contentId == 1">Fuel Quote

     </div>
      <div v-if="contentId == 2" style="padding: 0px 40px">
        <h2>Fuel Quote History</h2>
        <template>
          <el-table :data="tableData" stripe style="width: 100%; padding: 10px 0px" >
            <el-table-column prop="Order Date" label="Orde Date" width="180"></el-table-column>
            <el-table-column prop="Gallons Requested" label="Gallons Requested" width="180"></el-table-column>
            <el-table-column prop="Delivery Address" label="Delivery Address"  ></el-table-column>
            <el-table-column prop="Delivery Date" label="Delivery Date" width="180"></el-table-column>
            <el-table-column prop="Suggested Price" label="Suggested Price" width="180"></el-table-column>
            <el-table-column prop="Total Amount Due" label="Total Amount Due" width="180"></el-table-column>
          </el-table>
          <el-pagination
            background
            layout="prev, pager, next"
            :total="1000"
            stripe style="float: right;padding: 20px 30px">
          </el-pagination>
        </template>
      </div>
    </transition>
  </div>


</div>

</template>

<script>

  export default {
    name: "Login",
    data(){
      return {
        serverPrefix:'https://rap.dipath.cn/mockjsdata/41',
        activeIndex: '1',
        contentId: 1,
        tableData:[],
      }
    },
    mounted() {
      const vm = this;
      this.contentId = 1;

    },
    methods:{
      handleSelect(key, keyPath) {
          if(key==1){
              this.contentId = 1;
          }else if(key == 2){
              this.contentId = 2;
             this.getFuleQuoteHistory();
          }
//        console.log(key, keyPath);
      },
      getFuleQuoteHistory(){
        var that = this;
        var data = "3355";//userId
        var url=this.serverPrefix+"/getFuleQuoteHistory";
        this.$axios.get(url,data).then(function(res){
//          console.log(res.data.msg);
          var msg = res.data.msg;
          that.tableData = msg.quoteList;
          that.total = msg.total;
        },function(){
          console.log('error');
        });


    }
    },

    computed:{

    }
  }
</script>

<style>
  #nav-bar{
    box-shadow: 0px 7px 20px -5px #d7d7d7;
    height: 62px;
  }
  #container{
    padding: 0 100px;
  }
  #nav{
  	float: right;
  	display: flex;
    font-weight: 500;
  }
  .nav-brand-item{
    /*display: block;*/
    background-image:url("./../../static/img/fule icon.png");
    background-size: 60px 60px ;
    height: 60px;
    width: 60px;
    float: left;
    margin-left: 100px;
  }

  .user-account{
    height: 60px;
    width: 60px;
    float: right;
    line-height: 60px;
    color: #8f9397;
    font-size: 0.65rem;
    padding-left: 20px;
  }
  .main-container{
    min-height: calc(100vh - 50px);
    width: 100%;
    position: relative;
    overflow: hidden;

  }
  /*.el*/
  .el-table thead tr{
    background:  linear-gradient(150deg, #97c74e 0%, #2ab9a5 100%) ;
    color: white;
  }
  .el-table th, .el-table tr {
  background: #fff0;
  }
  .el-pagination.is-background .el-pager li:not(.disabled):hover {
    color:#43bc91;
  }
  .el-pagination.is-background .el-pager li:not(.disabled).active{
    background-color: #43bc91;
  }
</style>

