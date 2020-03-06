<template>
 <div class="all-container">
    <div id="nav-bar">
    <div id="container">
      <div class="nav-brand-item"></div>
      <div class="user-account" ><router-link to="/FuelQuote"><a style="margin-left: 5px">Home</a></router-link></div>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" id="nav"
               text-color="#8f9397"
               active-text-color="#4cbd89"
      >
      <el-menu-item index="1">Edit Profile</el-menu-item>
      <el-menu-item index="2">Edit Password</el-menu-item>
      </el-menu>


    </div>

  </div>
  <div class="main-container" >
    <transition name="fade-transform" mode="out-in">
      <div v-if="contentId == 1"style="padding: 20px 40px" >
        <el-form :model="userlist" :rules="rules" ref="EditorUserForms" label-width="300px" class="demo-ruleForm" style="margin: 0px 330px">
        <el-form-item label="User ID" prop="userid" :label-width="formLabelWidth" >
         <el-col :span="21"> <el-input v-model="userlist.userid" disabled ></el-input></el-col>
        </el-form-item>

        <el-form-item label="Full Name" prop="username" :label-width="formLabelWidth">
         <el-col :span="21">
          <el-input v-model="userlist.username" ></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="Address1" prop="address1" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.address1" placeholder="Please enter address required"></el-input></el-col>
        </el-form-item>

        <el-form-item label="Address2" prop="address2" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.address2" placeholder="Please enter address optional"></el-input></el-col>
        </el-form-item>

        <el-form-item label="City" prop="city" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.city" placeholder="Please enter city"></el-input></el-col>
        </el-form-item>

        <el-form-item label="State" prop="state" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.state" placeholder="Please enter state"></el-input></el-col>
         <country-select v-model="country" :country="country" topCountry="US" />
         <region-select v-model="region" :country="country" :region="region" />
        </el-form-item>

        <el-form-item label="ZipCode" prop="zipcode" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.zipcode" placeholder="Please enter Zipcode"></el-input></el-col>
        </el-form-item>

        <el-form-item >
         <el-col :span="21">  <el-button type="primary" @click="EditorUserClick('userlist')" >Save</el-button></el-input></el-col>
        </el-form-item>

      </el-form>
    </div>

    <div v-if="contentId == 2" style="padding: 20px 40px">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="300px" class="demo-ruleForm" style="margin: 0px 330px; text-align: center">
       <el-form-item label="Original Password" prop="pass" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="ruleForm.pass" placeholder="Please enter original password" type="password"></el-input></el-col>
        </el-form-item>
        <el-form-item label="New Password" prop="newpass" :label-width="formLabelWidth">
         <el-col :span="21"><el-input v-model="ruleForm.newpass" placeholder="Please enter new password" id="newkey" type="password"></el-input></el-col>
        </el-form-item>
        <el-form-item label="Repeat Password" prop="checknewpass" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="ruleForm.checknewpass" placeholder="Please enter new password again" id='newkey1' type="password"></el-input></el-col>
        </el-form-item>

        <el-form-item>
         <el-col :span="21">  <el-button type="primary" @click="submitForm('ruleForm')">save</el-button></el-col>
        </el-form-item>

        
        </el-form>
      
    </div>
  </transition>
  </div>

<!--     <div class="all-container-padding bg" >
     <el-tabs v-model="activeName" @tab-click="handleClick" >
     <el-tab-pane label="Profile" name="first" >
      <el-form :model="userlist" :rules="rules" ref="EditorUserForms">
        <el-form-item label="User ID" prop="userid" :label-width="formLabelWidth" >
         <el-col :span="8"> <el-input v-model="userlist.userid" disabled ></el-input></el-col>
        </el-form-item>

        <el-form-item label="User Name" prop="username" :label-width="formLabelWidth">
         <el-col :span="8">
          <el-input v-model="userlist.username" ></el-input>
          </el-col>
        </el-form-item>

        <el-form-item label="Address" prop="address" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="userlist.address" placeholder="Please enter address"></el-input></el-col>
        </el-form-item>

        <el-form-item label="City" prop="city" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="userlist.city" placeholder="Please enter city"></el-input></el-col>
        </el-form-item>

        <el-form-item label="State" prop="state" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="userlist.state" placeholder="Please enter state"></el-input></el-col>
        </el-form-item>

        <el-form-item label="ZipCode" prop="zipcode" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="userlist.zipcode" placeholder="Please enter Zipcode"></el-input></el-col>
        </el-form-item>

      </el-form>
      <div class="grid-content bg-purple">
       <el-button type="primary" @click="EditorUserClick('userlist')" >Save</el-button>
      </div>
     </el-tab-pane>
     <el-tab-pane label="Edit Password" name="second">
      <el-form :model="ruleForm" :rules="rules" ref="ruleForm">
       <el-form-item label="Original Password" prop="pass" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="ruleForm.pass" placeholder="Please enter original password" type="password"></el-input></el-col>
        </el-form-item>
        <el-form-item label="New Password" prop="newpass" :label-width="formLabelWidth">
         <el-col :span="8"><el-input v-model="ruleForm.newpass" placeholder="Please enter new password" id="newkey" type="password"></el-input></el-col>
        </el-form-item>
        <el-form-item label="Repeat Password" prop="checknewpass" :label-width="formLabelWidth">
         <el-col :span="8">  <el-input v-model="ruleForm.checknewpass" placeholder="Please enter new password again" id='newkey1' type="password"></el-input></el-col>
        </el-form-item>
        </el-form>
        <div class="grid-content bg-purple">
        <el-button type="primary" @click="submitForm('ruleForm')">save</el-button>
      </div>
     </el-tab-pane>
    </el-tabs>
    </div> -->
   </div>

</template>





<script>
//这些不要在意，这些是我们自定义的接口，用的时候就直接拿来了
// import {fetchAll,fetchByID,fetchList,postData,putData,deleteByID,deleteAllByID,guid,bytesToSize} from "@/api/dbhelper";
//这一步很重要，一般我们直接从后台拿过来输出来会是在data里面，但是我发现却在store里面，这里就要用到vuex
// import { mapGetters } from "vuex";
export default {
 data() {
/*****检验两次密码是否一致***/
  var validatePass = (rule, value, callback) => {
   if (value === "") {
    callback(new Error("请输入密码"));
   } else {
    if (this.ruleForm.checknewpass !== "") {
     this.$refs.ruleForm.validateField("checknewpass");
    }
    callback();
   }
  };
  var validatePass2 = (rule, value, callback) => {
   if (value === "") {
    callback(new Error("请再次输入密码"));
   } else if (value !== this.ruleForm.newpass) {
    callback(new Error("两次输入密码不一致!"));
   } else {
    callback();
   }
  };
  return {
   ruleForm: {},//修改密码的表单
   activeIndex: '1',
   contentId: 1,
   disabled:true,

   baseUrl: process.env.BASE_API,
   userlist: {},//用户信息表单
   formLabelWidth: "150px",
  /***校验***/
   rules: {
    address1: [{
      required: true,
      message: "please enter address1"
    }],
    address2: [{
      required: false
    }],
    city: [{
      required: true,
      message: "please enter city"
    }],
    state: [{
      required: true,
      message: "please enter state"
    }],
    zipcode: [{
      required: true,
      message: "please enter zipcode"
    },
    {
      pattern: /(^\d{5}$)|(^\d{5}-\d{4}$)/,
      message: "number only"
    }
    ],
    pass: [
     {
      required: true,
      trigger: "blur",
      message: "please enter original password"
     }
    ],
    newpass: [
     {
      validator: validatePass,
      trigger: "blur"
     }
    ],
    checknewpass: [
     {
      validator: validatePass2,
      trigger: "blur"
     }
    ]
   }
  };
 },
 created() {
  this.getUser();
  
 },


 // computed: {
 //  ...mapGetters(["username"])
 // },
mounted() {
      // const vm = this;
      this.contentId = 1;

    },
 methods: {

  handleSelect(key, keyPath) {
          if(key==1){
              this.contentId = 1;
          }else if(key == 2){
              this.contentId = 2;
             this.getFuleQuoteHistory();
          }
//        console.log(key, keyPath);
  },
  //获取个人用户的信息
  getUser() {
   postData("接口", this.username).then(response => {
    if (response.status === 200) {
     this.userlist = response.data;
     this.loading = false;
     console.log(this.userlist, 9696);
    } else {
     this.$message({
      message: "获取信息失败," + response.message,
      type: "error"
     });
    }
   });
  },
  // //tab切换
  // handleClick(tab, event) {
  //  console.log(tab, event);
  // },

  //修改密码
  submitForm(ruleForm) {
   var obj = {
    username: this.username,
    oldpwd: this.ruleForm.pass,
    newpwd: this.ruleForm.newpass
   };
   console.log(obj);
   postData("接口", obj).then(response => {
    if (response.status == 200) {
     this.$message({
      message: "保存成功",
      type: "success"
     });
    } else {
     this.$message({
      message: "修改失败" + response.message,
      type: "error"
     });
    }
   });
  },
  // 编辑提交的方法
  EditorUserClick() {
   this.$refs.EditorUserForms.validate(valid => {
    if (valid) {
     console.log(this.userlist);
     putData("接口", this.userlist).then(response => {
      if (response.status == 200) {
       this.$message({
        message: "编辑成功",
        type: "success"
       });
      } else {
       this.$message({
        message: "修改失败" + response.message,
        type: "error"
       });
      }
     });
    }
   });
  }
 }
};
</script>

<style type="text/css">
/*.el-tabs__item{
    background-image:url("./../../static/img/fule icon.png");
    background-size: 60px 60px ;
    height: 60px;
    width: 60px;
    float: left;
    margin-left: 100px;
}*/

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
  .main-container{
    min-height: calc(100vh - 50px);
    width: 100%;
    position: relative;
    overflow: hidden;
    font-family: "Roboto", sans-serif !important;

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
  /*.el*/
  .el-table thead tr{
    background:  linear-gradient(150deg, #97c74e 0%, #2ab9a5 100%) ;
    color: white;
  }
  .el-table th, .el-table tr {
  background: #fff0;
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
  .user-account{
    height: 60px;
    width: 60px;
    float: right;
    line-height: 60px;
    color: #8f9397;
    font-family: "Roboto", sans-serif !important;
    padding-left: 20px;
  }
</style>