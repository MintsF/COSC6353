<!-- <template> -->
    <!-- <div class="username">  -->
        <!-- <div class="input_style">	 -->
  	      <!-- <el-input placeholder="Username" v-model="name" clearable  ></el-input> -->
  	    <!-- </div> -->
    <!-- </div> -->
<!-- // </template> -->

<!-- <script></script> -->

<!-- <style>
/* // .header {
//     background-color:red;
//     font-size: 40px;
// } */
/* // </style> */ -->




<template>
<div>
  <div class="leftside" style="width: 30%">Hi this is leftside</div>
  <div class="rightside" style="width: 50%">
  	<div style="width: 25%;float: left">Hi this is rightside</div>
  	<div class="profile" style="width: 73%;float: left">
  	  <!-- <div class="logo"  > gas price prediction</div> -->
  	  <h2>Create your profile!</h2>
  	  <h5>Nice to see you! Please create your personal profile!</h5>

  	  <div class="block1" >
  	  	<div class="tag1" ><span style="display: line-block; vertical-align: text-bottom;"><strong>Full Name</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Username" v-model="name" clearable  ></el-input>
  	    </div>
  	  </div>

  	  <div class="block1" >
  	  	<div class="tag1" ><span><strong>*Password</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="********" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>

      <div class="block1" >
  	  	<div class="tag1" ><span><strong>*Address1</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Address1" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>
    
      <div class="block1" >
  	  	<div class="tag1" ><span><strong>Address2</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Address2" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>
      
      <div class="block1" >
  	  	<div class="tag1" ><span><strong>*City</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="City" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>
      
      <div class="block1" >
  	  	<div class="tag1" ><span><strong>*State</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="State" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>

      <div class="block1" >
  	  	<div class="tag1" ><span><strong>*Zipcode</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Zipcode" v-model="pwd" show-password   ></el-input>
  	    </div>
  	  </div>






      <div >
        <el-button type="primary" @click="login" class="login_style">Submit</el-button>
      </div>
      <!-- <div>
        <div class="tag2"><a href="" style="color: gray">forget password</a></div>
        <div class="tag2"><a href="" style="color: gray">Sign Up</a></div>
      </div> -->
    </div> 	
  </div>
</div>

</template>

<script>

  export default {
    name: "Login",
    data(){
      return {
        name: '',
        pwd : ''   
      }
    },
    methods:{
      login(){
        
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
    min-height: 150vh;
    flex-direction: column;

    background: linear-gradient(#97C74F,#2BB9A5);

  }
  .rightside{
	width: 70%;
	float: left;
/*	border-style: solid;
	border-width: 5px;*/
	/*display: flex;*/
    min-height: 100vh;
    flex-direction: column;

  }

  .profile{
/*  	border-style: solid;
	border-width: 2px;
	border-color: red;*/
	margin-top: 100px;

	text-align: center;
	vertical-align: center;
/*	min-height: 100vh;
    flex-direction: column;*/
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
/*  	border-style: solid;
	border-width: 2px;
	border-color: yellow;
	float: center;*/
	margin-bottom: 20px;
  }
  .tag1{
  	width:fit-content;


  	/*text-align: center;*/
  	/*display:inline-block;*/
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
    /*transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;*/

  }
  .login_style{
    /*width: 300px;*/
    background-color: lightgreen;
  }
  .tag2{
  	height: auto;
  	margin-top: 10px;
  }

</style>



