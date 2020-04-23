
<template>
<div >
  <div id="nav-bar">
    <div id="container">
      <div class="nav-brand-item"></div>
      <span class="nav-brand-txt">
        Fuel Quote System
      </span>
      <div class="user-account" @click="logout()"><i class="el-icon-user-solid"><span style="margin-left: 5px">Logout</span></i></div>
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
             <!-- v-on:input="getPrice()"  -->
             <!-- gallonsKeyup() -->
             <!-- v-on:input="gallons()" -->
             <el-col :span="21"><el-input v-model="ruleForm.gallonsRequested" oninput="value=value.replace(/[^0-9.]/g,'')" v-on:input="gallons()"  placeholder="please input  Gallons Requested"></el-input></el-col>
             <el-col :span="1">Gal.</el-col>
           </el-form-item>
           <el-form-item label=" Deliver Date" required prop="deliveryDate">
             <el-date-picker type="date"  @change="dateChange" v-on:input="getPrice()" value-format="yyyy-MM-dd"  placeholder="please select delivery Date" v-model="ruleForm.deliveryDate" :picker-options="pickerOption" style="width: 100%;"></el-date-picker>
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
             <!-- <el-button type="success" @click="getPrice('ruleForm')">Get Price</el-button> -->
             <el-button type="success" @click="submitForm('ruleForm')">Submit</el-button>
             <el-button @click="resetForm('ruleForm')">Reset</el-button>
           </el-form-item>
         </el-form>
      </div>
      <div v-if="contentId == 2" style="padding: 0px 40px">
        <h2>Fuel Quote History</h2>
        <template>
          <el-table :data="tableData" stripe style="width: 100%; padding: 10px 0px" >
            <!-- <el-table-column prop="orderDate" label="Orde Date" width="180"></el-table-column> -->
            <el-table-column prop="gallonsRequested" label="Gallons Requested" width="180"></el-table-column>
            <el-table-column prop="deliveryAddress" label="Delivery Address"  ></el-table-column>
            <el-table-column prop="deliveryDate" label="Delivery Date" width="180"></el-table-column>
            <el-table-column prop="suggestedPrice" label="Suggested Price" width="180"></el-table-column>
            <el-table-column prop="totalAmountDue" label="Total Amount Due" width="180"></el-table-column>
          </el-table>
<!--           <el-pagination
            background
            @current-change = "handleChangePage"
            layout="prev, pager, next"
            :page-size="5"
            :total="total"
            :current-page.sync="currentPage"
            stripe style="float: right;padding: 20px 30px">
          </el-pagination> -->
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
          deliveryDate: '',
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
            // { type: 'number',  message: 'Gallons Requested must be a positive number', trigger: 'blur' },
            // { 
            //   validator (rule, value, callback) {
            //     if (/(^[0-9]\d*$)/.test(value)) {
            //       callback()
            //     }else {
            //       callback(new Error('please input a positive number'))
            //     }
            //     },trigger: 'blur'
            // }
          ],
          deliveryDate: [
            // { type: 'date', required: true, message: 'please select deliver Date', trigger: 'change' },
            { required: true, message: 'please select deliver Date', trigger: 'change' },

          ],

        },

        pickerOption: {
        disabledDate(time) {
          return time.getTime() < Date.now() - 8.64e7;
          },
        },
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
        console.log("userInfo: "+ userInfo);
        // var userName = "11223344";
        this.userName = userInfo;
        var postData =this.$qs.stringify ({
          username:  that.userName,
        });


        this.$axios.post('/api/getOrderHistory/',postData).then(function(res){
          var msg = res.data;
          console.log(res);
          if(msg.code==4001)
            that.profile.isRequestedFuel=1;
          console.log("get History");
          console.log(that.profile.isRequestedFuel);

        },function(){
          console.log('error');
        });


        this.$axios.post('/api/getUserProfile/',postData).then(function(res){
          console.log(res.data);
          that.profile = res.data.profile;
          that.ruleForm.deliveryAddress = that.profile.address1 +that.profile.address2+", "+ that.profile.city +", "+ that.profile.state +" "+ that.profile.zipCode;
        },function(){
          console.log('error');
        });
      },
      goToProfile(){
        this.$router.push('/Profile');
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
      dateChange(val){
        // console.log(val);
        this.ruleForm.deliveryDate = val;
        console.log(this.ruleForm.deliveryDate );
      },
  
      gallons(){
        var that = this;
        // console.log("gallons")
        if(parseFloat(that.ruleForm.gallonsRequested).toString() == "NaN"){
            console.log("The input is not a number")
            this.ruleForm.gallonsRequested = ' '
            this.ruleForm.suggestedPrice = ' '
            this.ruleForm.totalAmountDue = ' '
        }else{         
            if(that.ruleForm.gallonsRequested < 0){
                that.ruleForm.gallonsRequested = ' '
                this.ruleForm.suggestedPrice = ' '
                this.ruleForm.totalAmountDue = ' '
            }else{
                // console.log("get Price now")
                this.getPrice()
            }
        }
      },
      getPrice(){
          var that = this;
          // alert("getPrice");
         if(that.ruleForm.gallonsRequested == ' '){
            this.ruleForm.suggestedPrice = ' '
            this.ruleForm.totalAmountDue = ' '
            return;
         }
        if(that.ruleForm.deliveryAddress !='' && that.ruleForm.deliveryDate !='' ){
            var locationFactor=0.04;
            var currentPrice = 1.5;
            var rateHistoryFactor=0;
            var gallonsRequestedFactor = 0.03;
            var companyProfitFactor = 0.1;
            var rateFluctuation = 0.03;
            var curDate = new Date(this.ruleForm.deliveryDate)
            var curMonth = curDate.getMonth()+1;
            if(this.profile.state=="Texas"||this.profile.state=="TX") {
              locationFactor = 0.02;
            }
            if(this.profile.isRequestedFuel != 0){
              rateHistoryFactor = 0.01;
            }
            if(this.ruleForm.gallonsRequested >=1000){
              gallonsRequestedFactor = 0.02
            }
            if(curMonth>='4' &&curMonth<='6'){
              rateFluctuation=0.04;
            }
    //        if(ruleForm.deliveryDate)
            var margin = currentPrice * (locationFactor - rateHistoryFactor + gallonsRequestedFactor + companyProfitFactor + rateFluctuation)
            var suggestedPrice = currentPrice + margin;
            this.ruleForm.suggestedPrice = suggestedPrice;
            // alert(this.ruleForm.gallonsRequested);
            this.ruleForm.totalAmountDue = suggestedPrice* this.ruleForm.gallonsRequested;
            // alert(this.ruleForm.gallonsRequested);
        }else{
            // alert("please enter required info");
        }
      },
      submitForm(formName) {
        console.log("submit order")
        var that = this;
        console.log("ddsd"+that.userName);
        console.log(this.ruleForm);
        var postData =this.$qs.stringify ({
          username: that.userName,
          gallonsRequested : that.ruleForm.gallonsRequested,
          deliveryAddress: that.ruleForm.deliveryAddress,
          deliveryDate : that.ruleForm.deliveryDate,
          suggestedPrice :  that.ruleForm.suggestedPrice,
          totalAmountDue : that.ruleForm.totalAmountDue
        });
        console.log(postData)
        alert(typeof(that.ruleForm.gallonsRequested))
        if(that.ruleForm.gallonsRequested !=''&& that.ruleForm.deliveryAddress !='' && that.ruleForm.deliveryDate !='' && that.ruleForm.suggestedPrice!='' && that.ruleForm.totalAmountDue!='' ){
          that.$axios.post('/api/submitOrder/',postData).then(function(res){
              that.$message({
                 message: 'sumbit success',
                 type: 'success'
              });
          },function(){
            console.log('error');
          });
        }else{          
                 that.$message({
                 message: 'please enter the require info',
                type: 'warning'
              }); 
        }
       
      },
      resetForm(formName) {
        // this.$refs[formName].resetFields();

        this.ruleForm.gallonsRequested='';
        // this.ruleForm.deliveryAddress: '',
        this.ruleForm.deliveryDate='';
        this.ruleForm.suggestedPrice='';
        this.ruleForm.totalAmountDue='';
        // console.log(this.profile.address);
      },
      getFuleQuoteHistory(){
        var that = this;
        console.log(that.userName);

        var postData =this.$qs.stringify ({
          username: that.userName,
        });
        this.$axios.post('/api/getOrderHistory/',postData).then(function(res){
          var msg = res.data;
          console.log(res);
          that.tableData = msg.orderList;
          console.log(that.tableData)
          that.total = msg.total;
        },function(){
          console.log('error');
        });

    },

    logout(){
      localStorage.removeItem('username');
      console.log(localStorage.getItem('username'));
      this.$router.push('/');

    }

    // handleChangePage(val){
    //   this.currentPage=val;
    //   this.getFuleQuoteHistory();
    // }
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

