
 <template>
  <div class="login">
  	<div class="logo" > gas price prediction</div>
    <div>
      <el-input placeholder="Username" v-model="name" clearable class="input_style"></el-input>
    </div>
    <div>
      <el-input placeholder="Password" v-model="pwd" show-password class="input_style"></el-input>
    </div>
    <div>
      <el-button type="primary" @click="login" class="login_style">Sign In</el-button>
    </div>
    <div>
      <div>
      	<a href="">forget password</a>
      </div>
      <div>
      	<a href="">Sign Up</a>
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
  .login{
    margin-top: 200px;
  }
  .logo{
  	font-family: "DejaVu Sans Mono";
  	color: lightblue;
  	text-align: center;
  	font-size: 30px;
    margin-bottom: 30px;
  }
  .input_style{
    width: 300px;
    margin-bottom: 30px;
  }
  .login_style{
    width: 300px;
  }

</style>


