
<template>
<div >
  <div id="nav-bar">
    <div id="container">
      <div class="nav-brand-item"></div>
      <span class="nav-brand-txt">
        Fuel Quote System
      </span>
      <div class="user-account" @click="goToProfile()"><i class="el-icon-user-solid"><span style="margin-left: 5px">Account</span></i></div>
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
      <div v-if="contentId == 1"style="padding: 0px 40px">
         <h2>Fuel Quote </h2>
         <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="200px" class="demo-ruleForm" style="margin: 0px 330px">
           <el-form-item label="Gallons Requested" required prop="gallonsRequested">
             <el-col :span="21"><el-input v-model="ruleForm.gallonsRequested" placeholder="please input  Gallons Requested"></el-input></el-col>
             <el-col :span="1">Gal.</el-col>
           </el-form-item>
           <el-form-item label=" Deliver Date" required prop="deliverDate">
             <el-date-picker type="date" placeholder="please select deliver Date" v-model="ruleForm.deliverDate" style="width: 100%;"></el-date-picker>
           </el-form-item>
           <el-form-item label=" Delivery Address"  prop="deliveryAddress" >
             <el-input v-model="ruleForm.deliveryAddress" placeholder="please input delivery address" readonly="readonly"></el-input>
           </el-form-item>
           <el-form-item label=" Suggested Price"  prop="suggestedPrice">
             <el-col :span="21"><el-input v-model="ruleForm.suggestedPrice"  readonly="readonly"></el-input></el-col>
             <el-col :span="1">$</el-col>
           </el-form-item>
           <el-form-item label=" Total Amount Due"  prop="totalAmountDue">
             <el-col :span="21"><el-input v-model="ruleForm.totalAmountDue"  readonly="readonly"></el-input></el-col>
             <el-col :span="1">$</el-col>
           </el-form-item>
           <el-form-item>
             <el-button type="success" @click="getPrice('ruleForm')">Get Price</el-button>
             <el-button type="success" @click="submitForm('ruleForm')">Submit</el-button>
             <el-button @click="resetForm('ruleForm')">Reset</el-button>
           </el-form-item>
         </el-form>
      </div>
      <div v-if="contentId == 2" style="padding: 0px 40px">
        <h2>Fuel Quote History</h2>
        <template>
          <el-table :data="tableData" stripe style="width: 100%; padding: 10px 0px" >
            <el-table-column prop="orderDate" label="Orde Date" width="180"></el-table-column>
            <el-table-column prop="gallonsRequested" label="Gallons Requested" width="180"></el-table-column>
            <el-table-column prop="deliveryAddress" label="Delivery Address"  ></el-table-column>
            <el-table-column prop="deliveryDate" label="Delivery Date" width="180"></el-table-column>
            <el-table-column prop="suggestedPrice" label="Suggested Price" width="180"></el-table-column>
            <el-table-column prop="totalAmountDue" label="Total Amount Due" width="180"></el-table-column>
          </el-table>
          <el-pagination
            background
            @current-change = "handleChangePage"
            layout="prev, pager, next"
            :page-size="5"
            :total="total"
            :current-page.sync="currentPage"
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
        serverPrefix:'https://www.fastmock.site/mock/b9af25ea0ab3dd7bc9695d3c606dc608/fule',
        activeIndex: '1',
        contentId: 1,
        tableData:[],
        total:0,

        currentPage:1,
        submitDisabled:true,
        ruleForm: {
          gallonsRequested:'',
          deliveryAddress: '',
          deliverDate: '',
          suggestedPrice:'',
          totalAmountDue:''
        },
        profile:{
          userName: "",
          address:"",
          city: "",
          state:"",
          zipCode:0,
          isRequestedFuel:0
        },
        userName:'',
        rules: {
          gallonsRequested: [
            { required: true,  message: 'please enter  Gallons Requested', trigger: 'blur' },
//            { type: 'number',  message: 'Gallons Requested must be a positive integer', trigger: 'blur' }
          ],
          deliverDate: [
            { type: 'date', required: true, message: 'please select deliver Date', trigger: 'change' }
          ],

        }
      }
    },
    mounted() {
      const vm = this;
      this.contentId = 1;
      this.getUserProfile();
    },
    methods:{
      getUserProfile(){
        var that = this;
        var userInfo = localStorage.getItem('username');
        var userName = "11223344";
        this.userName = userName;
        var postData =this.$qs.stringify ({
          username: '11223344',
        });
        this.$axios.post('/api/getUserProfile/',postData).then(function(res){
          that.profile = res.profile;
          that.ruleForm.deliveryAddress = that.profile.address +", "+ that.profile.city +", "+ that.profile.state +" "+ that.profile.zipCode;
        },function(){
          console.log('error');
        });
      },
      goToProfile(){
        this.$router.push('/HelloWorld');
      },
      handleSelect(key, keyPath) {
          if(key==1){
              this.contentId = 1;
          }else if(key == 2){
              this.contentId = 2;
             this.getFuleQuoteHistory();
          }
//        console.log(key, keyPath);
      },
      getPrice(){
        var locationFactor=0.04;
        var currentPrice = 1.5;
        var rateHistoryFactor=0;
        var gallonsRequestedFactor = 0.03;
        var companyProfitFactor = 0.1;
        var rateFluctuation = 0.03;
        if(this.profile.state=="Texas"||this.profile.state=="TX") {
          locationFactor = 0.02;
        }
        if(this.profile.isRequestedFuel != 0){
          rateHistoryFactor = 0.01;
        }
        if(this.ruleForm.gallonsRequested >=1000){
          gallonsRequestedFactor = 0.02
        }
//        if(ruleForm.deliverDate)
        var margin = currentPrice * (locationFactor - rateHistoryFactor + gallonsRequestedFactor + companyProfitFactor + rateFluctuation)
        var suggestedPrice = currentPrice + margin;
        this.ruleForm.suggestedPrice = suggestedPrice;
        this.ruleForm.totalAmountDue = suggestedPrice* this.ruleForm.gallonsRequested;
      },
      submitForm(formName) {
////             ruleForm: {
//        gallonsRequested:'',
//          deliveryAddress: '',
//          deliverDate: '',
//          suggestedPrice:'',
//          totalAmountDue:''
//      },
        console.log("submit order")
        var that = this;
        var postData =this.$qs.stringify ({
          username: that.userName,
          gallonsRequested : that.ruleForm.gallonsRequested,
          deliveryAddress: that.ruleForm.deliveryAddress,
          deliverDate : that.ruleForm.deliverDate,
          suggestedPrice :  that.ruleForm.suggestedPrice,
          totalAmountDue : that.ruleForm.totalAmountDue
        });
        this.$axios.post('/api/submitOrder/',postData).then(function(res){
          that.profile = res.profile;
          that.ruleForm.deliveryAddress = that.profile.address +", "+ that.profile.city +", "+ that.profile.state +" "+ that.profile.zipCode;
        },function(){
          console.log('error');
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      getFuleQuoteHistory(){
        var that = this;
        var postData =this.$qs.stringify ({
          username: '11223344',
        });

        var postData =this.$qs.stringify ({
          username: that.userName,
          gallonsRequested : that.ruleForm.gallonsRequested,
          deliveryAddress: that.ruleForm.deliveryAddress,
          deliverDate : that.ruleForm.deliverDate,
          suggestedPrice :  that.ruleForm.suggestedPrice,
          totalAmountDue : that.ruleForm.totalAmountDue
        });
        this.$axios.post('/api/orderHistory/',postData).then(function(res){
          var msg = res.data.msg;
          that.tableData = msg.orderList;
          that.total = msg.total;
        },function(){
          console.log('error');
        });

    },

    handleChangePage(val){
      this.currentPage=val;
      this.getFuleQuoteHistory();
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
    font-family: "Roboto", sans-serif !important;
  }
  #nav{
  	float: right;
  	display: flex;
    font-weight: 500;
    /*font-family: "Roboto", sans-serif !important;*/
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
  .nav-brand-txt{
    height: 60px;
    line-height: 60px;
    float: left;
    font-family: Trajan Pro;
    font-weight: 600;
  }
  .user-account{
    height: 60px;
    width: 60px;
    float: right;
    line-height: 60px;
    color: #8f9397;
    font-size: 0.65rem;
    padding-left: 20px;
    cursor:pointer;
  }
  .main-container{
    min-height: calc(100vh - 50px);
    width: 100%;
    position: relative;
    overflow: hidden;
    font-family: "Roboto", sans-serif !important;

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

  .el-button--success{
    font-family: "Roboto", sans-serif;
    font-weight: 600;
    background:linear-gradient(150deg,  #97c74e 0%, #2ab9a5 100%);
  }
  .el-button--success:hover,.el-button--success:focus{
    color: #ffffff;
    background:linear-gradient(330deg,  #97c74e 0%, #2ab9a5 100%);
  }
</style>

