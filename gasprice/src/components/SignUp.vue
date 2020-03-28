
<template>
<div>
  <div class="leftside" style="width: 30%"></div>
  <div class="rightside" style="width: 50%">
    <div style="width: 25%;float: left"></div>
    <div class="signup" style="width: 73%;float: left">
      <!-- <div class="logo"  > gas price prediction</div> -->
      <h2>Sign up for your account!</h2>
      <h5>Join us today! Create your account easy with less information.</h5>

      <div class="block1" >
        <div class="tag1" ><span style="display: line-block; vertical-align: text-bottom;"><strong>Username</strong></span></div>
        <div class="input_style"> 
          <el-input placeholder="Username" v-model="userInfo.name" clearable  ></el-input>
        </div>
      </div>

      <div class="block1" >
        <div class="tag1" ><span><strong>Password</strong></span></div>
        <div class="input_style"> 
          <el-input placeholder="********" v-model="userInfo.pwd" show-password   ></el-input>
        </div>
      </div>

      <div class="block1" >
        <div class="tag1" ><span><strong>Confirm Password</strong></span></div>
        <div class="input_style"> 
          <el-input placeholder="********" v-model="userInfo.cpwd" show-password   ></el-input>
        </div>
      </div>

      <div >
        <el-button type="primary" @click="signup" class="signup_style">Sign me Up!</el-button>
      </div>
      <div>
        <div class="tag2"><router-link to="/"><a  style="color: gray">Sign In</a></router-link></div>
        <!-- <div class="tag2"><a href="" style="color: gray">Sign me Up!</a></div> -->
      </div>
    </div>  
  </div>
</div>

</template>

<script>

  export default {
    name: "SignUp",
    data(){
      return {
        userInfo: {
          name: '',
          pwd : '',
          cpwd: '',

        }
      }
    },
    methods:{
      signup(){
        var name=this.userInfo.name;
        name= name.replace(/\s+/g,"");
        var password= this.userInfo.pwd;
        var confirmpassword=this.userInfo.cpwd;
        if (name==''){
          alert('userName can not be none');
            return false;
        }
        var reg = /^[\d]+$/;
        // var s = reg.test(name);
        // console.log(s);
        console.log(name.length);
        // console.log((name>=10000000));
        if(name.length !=8){
          alert('user name must be 8 characters without space');
          return false;
        }


        if(password==''&&password.trim()==password ){
          alert('password can not be none and can not include space');
          return false;
        }

        if(confirmpassword=='' && confirmpassword.trim()==confirmpassword ){
          alert('confirm password can not be none and can not include space');
          return false;
        }

        
        if(confirmpassword!=password){
          alert('password do not match, please try again');
          return false;
        }

        var postData =this.$qs.stringify ({
          username: this.userInfo.name,
          password: this.userInfo.pwd,
        });
        this.$axios.post('/api/register/',postData).then(res=>{
          // this.$router.push({path:'/login'})
          console.log(res)
        }, function(){
          console.log("sign up can not connect to server");
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
/*  border-style: solid;
  border-width: 5px;*/
  /*display: flex;*/
    min-height: 100vh;
    flex-direction: column;

  }

  .signup{
/*    border-style: solid;
  border-width: 2px;
  border-color: red;*/
  margin-top: 100px;

  text-align: center;
  vertical-align: center;
/*  min-height: 100vh;
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
/*    border-style: solid;
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
  .signup_style{
    /*width: 300px;*/
    background-color: lightgreen;
  }
  .tag2{
    height: auto;
    margin-top: 10px;
  }

</style>



