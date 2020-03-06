
<template>
<div >
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
      <div v-if="contentId == 1"style="padding: 0px 40px">
         <h2>Fuel Quote </h2>
         <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="200px" class="demo-ruleForm" style="margin: 0px 330px">
           <el-form-item label="Gallons Requested" required prop="GallonsRequested">
             <el-col :span="21"><el-input v-model="ruleForm.GallonsRequested" placeholder="please input  Gallons Requested"></el-input></el-col>
             <el-col :span="1">Gal.</el-col>
           </el-form-item>
           <el-form-item label=" Delivery Address" required prop="DeliveryAddress">
             <el-input v-model="ruleForm.DeliveryAddress" placeholder="please input delivery address"></el-input>
           </el-form-item>
           <el-form-item label=" Deliver Date" required prop=" DeliverDate">
             <el-date-picker type="date" placeholder="please select deliver Date" v-model="ruleForm.DeliverDate" style="width: 100%;"></el-date-picker>
           </el-form-item>
           <el-form-item label=" Suggested Price"  prop="SuggestedPrice">
             <el-col :span="21"><el-input v-model="ruleForm.DeliveryAddress"  readonly="readonly"></el-input></el-col>
             <el-col :span="1">$</el-col>
           </el-form-item>
           <el-form-item label=" Total Amount Due"  prop="TotalAmountDue">
             <el-col :span="21"><el-input v-model="ruleForm.DeliveryAddress"  readonly="readonly"></el-input></el-col>
             <el-col :span="1">$</el-col>
           </el-form-item>
           <el-form-item>
             <el-button type="success" @click="getPrice('ruleForm')">Get Price</el-button>
             <el-button type="success" @click="submitForm('ruleForm')" disabled="disabled">Submit</el-button>
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
        disabled:true,
        ruleForm: {
          GallonsRequested: '',
          DeliveryAddress: '',
          DeliverDate: '',
        },
        rules: {
          GallonsRequested: [
            { required: true,  message: 'please input  Gallons Requested', trigger: 'blur' },
            { type: 'number',message: 'Gallons Requested must be a positive integer', trigger: 'blur' }
          ],
          DeliveryAddress: [
            { required: true, message: 'please input delivery address', trigger: 'change' }
          ],
          DeliverDate: [
            { type: 'date', required: true, message: 'please select deliver Date', trigger: 'change' }
          ],

        }
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
      getPrice(){

      },
      submitForm(formName) {
//        this.$refs[formName].validate((valid) => {
//          if (valid) {
//            alert('submit!');
//          } else {
//            console.log('error submit!!');
//            return false;
//          }
//        });
//        console.log(formName);
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
      getFuleQuoteHistory(){
        var that = this;
        var data = {
          userId:this.userId,
          currentPage: this.currentPage
        }
        var url=this.serverPrefix+"/getFuelQuoteHistory";
        this.$axios.get(url,data).then(function(res){
//          console.log(res.data.msg);
          var msg = res.data.msg;
          that.tableData = msg.quoteList;
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

