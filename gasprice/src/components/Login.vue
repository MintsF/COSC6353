<template>
<div>
  <div class="leftside" style="width: 30%">jjjjjj</div>
  <div class="rightside" style="width: 50%">
  	<div style="width: 25%;float: left">fff</div>
  	<div class="login" style="width: 73%;float: left">
  	  
  	  <h2>Sign into your account!</h2>
  	  <h5>Nice to see you! Please log in with your account.</h5>

  	  <div class="block1" >
  	  	<div class="tag1" ><span style="display: line-block; vertical-align: text-bottom;"><strong>Username</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Username" v-model="userInfo.userName" clearable  ></el-input>
  	    </div>
  	  </div>

  	  <div class="block1" >
  	  	<div class="tag1" ><span><strong>Password</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="********" v-model="userInfo.userPassword" show-password   ></el-input>
  	    </div>
  	  </div>

      <div >
        <el-button type="primary" @click="login" class="login_style">Sign In</el-button>
      </div>

      <div>
        <div class="tag2"><a href="" style="color: gray">forget password</a></div>
        <div class="tag2"><a href="" style="color: gray">Sign Up</a></div>
      </div>

    </div> 	
  </div>
</div>

</template>

<script>
// import axios from '../../node_modules/axios';

window.axios = require('axios');
export default {
    name: "Login",
    data(){
      return {
      	userInfo: {
      		userName: '',
      		userPassword: '',

      	}
    
      }
    },
    methods:{
      login(){
      	if (this.userInfo.userName==''){
      		alert('userName can not be none');
            return false;
      	}

      	if(this.userInfo.userPassword==''){
      		alert('password can not be none');
      		return false;
      	}

      	 this.axios({
      	 	methods: 'post',
      	 	url: '/login',
      	 	data: this.userInfo
      	 }).then(res=>{
      	 	console.log(res.data)
      	 })



     }

    }
  }
</script>

<style>
  .leftside{
  	/*border-style: solid;*/
	/*border-width: 5px;*/
  	/*border-color: red;*/
  	float: left;
  	/*height: auto;*/
  	display: flex;
    min-height: 100vh;
    flex-direction: column;

    background: linear-gradient(#97C74F,#2BB9A5);

  }
  .rightside{
	width: 70%;
	float: left;
    min-height: 100vh;
    flex-direction: column;

  }

  .login{
	margin-top: 100px;
	text-align: center;
	vertical-align: center;

  }

  .logo{
  	font-family: "DejaVu Sans Mono";
  	color: lightgreen;
  	text-align: center;
  	font-size: 30px;
    margin-top: 50px;
  }
  .block1{
  	width: 60%;
  	display:inline-block;
  	text-align: center;
	margin-bottom: 20px;
  }
  .tag1{
  	width:fit-content;
    height: 30px;
/*    border-style: solid;
	border-width: 2px;
	border-color: yellow;*/

  }
  .input_style{
    width: auto;
    height: auto;
    color: #495057;
    background-color: #ffffff;
    border: 2px solid #dfe2e5;
    border-radius: 3px;
    box-shadow: 0 0 15px lightgreen;

  }
  .login_style{
    background-color: lightgreen;
  }
  .tag2{
  	height: auto;
  	margin-top: 10px;
  }

</style>

