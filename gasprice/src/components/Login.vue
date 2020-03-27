<template>
<div>
  <div class="leftside" style="width: 30%">
  </div>
  <div class="rightside" style="width: 70%">
  	<div style="width: 25%;float: left">

    </div>
  	<div class="login" style="width: 75%;float: left">

  	  <h2>Sign into your account!</h2>
  	  <h5>Nice to see you! Please log in with your account.</h5>


  	  <div class="block1" >
  	  	<div class="tag1" ><span style="display: line-block; vertical-align: text-bottom;"><strong>Username</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="Username" v-model="userInfo.username" clearable  ></el-input>
  	    </div>
  	  </div>

  	  <div class="block1" >
  	  	<div class="tag1" ><span style="display: line-block; vertical-align: text-bottom;"><strong>Password</strong></span></div>
  	    <div class="input_style">	
  	      <el-input placeholder="********" v-model="userInfo.password" show-password   ></el-input>
  	    </div>
  	  </div>

      <div >
        <el-button type="primary" @click="login" class="login_style">Sign In</el-button>
      </div>

      <div>
        <div class="tag2"> <router-link to=""><a  style="color: gray">forget password</a></router-link> </div>
        <div class="tag2"><router-link to="/SignUp"><a  style="color: gray">Sign Up</a></router-link></div>
      </div>


    </div>
  </div>
</div>

</template>


<script >

export default {
    name: "Login",
    data(){
      return {

      	logining: false,
      	userInfo: {
      		username: '',
      		password: '',

      	}

      }
    },
    mounted() {

    },

    methods:{
      login(){
      	// var name=parseInt(this.userInfo.username);
        var name = this.userInfo.username
      	var password=this.userInfo.password;
        console.log("-----------");
        console.log(this.userInfo.username);
        console.log(this.userInfo.password);
      	if (name==''){
      		alert('userName can not be none');
            return false;
      	}

      	if(password==''){
      		alert('password can not be none');
      		return false;
      	}

        var postData =this.$qs.stringify ({
          username: this.userInfo.username,
          password: this.userInfo.password,
        });

        this.$axios.post('/api/login/',postData).then(res=>{
          console.log("connect to server success");
          console.log(res.data);
          // localStorage.setItem(this.userInfo,use)
          localStorage.setItem('username',JSON.stringify(res.data.username));
          localStorage.setItem('password',JSON.stringify(res.data.password));


          if (res.data.code==1002){
            if(res.data.flag!=0)
              this.$router.push('/FuelQuote')
            else
              this.$router.push('/HelloWorld')
          }

        }).catch((err)=>{
          console.log("can not connect to server");
        })

     }

    }
  }
</script>

<style>


  .leftside{

  	float: left;
  	display: flex;
    min-height: 100vh;
    flex-direction: column;

    background: linear-gradient(#97C74F,#2BB9A5);

  }
  .rightside{
	width: 70%;
	float: left;
    /*min-height: 100vh;*/
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
/*
	border-style: solid;
	border-width: 2px;
	border-color: red;*/
  }
  .tag1{
  	width:fit-content;
    /*height: 40px;*/
    text-align: left;


  }
  .input_style{
    /*width: auto;*/
    width:400px;
    /*height: auto;*/
    color: #495057;
    background-color: #ffffff;
    /*border: 2px solid #dfe2e5;*/
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

