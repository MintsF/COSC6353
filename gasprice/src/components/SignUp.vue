
 <template>
  <div class="signUp">
  	<div class="logo" > gas price prediction</div>
    <div>
      <el-input placeholder="Username" v-model="name" clearable class="input_style"></el-input>
      <span>{{msgname}}</span>
    </div>
    <div>
      <el-input placeholder="Password" v-model="password" show-password class="input_style"></el-input>
      <span>{{msgpassword}}</span>
    </div>
    <div>
      <el-input placeholder="Confirm password" v-model="confirmPassword" show-password class="input_style"></el-input>
      <span>{{msgConfirmPassword}}</span>
    </div>
    <div>
      <el-button type="primary" @click="signUp" class="signUp_style">Sign Up</el-button>
    </div>
 
  </div>
</template>

<script>
  export default {
    name: "Signup",
    data(){
      return {
        name: '',
        password : '',
        confirmPassword: '',
        msgname: '',
        msgpassword: '',
        msgConfirmPassword: ''

      }
    },
    methods:{
      signUp(){
        
      },
      checkname:function(){
        if(this.name.length==0){
          this.msgname="Username can not be null";
        }else if(this.name.length<2){
          this.msgname="Username at least two signal";
        }else{
          this.msgame="";
        }
        return this.name>2;
      },
      checkpassword:function(){
        var word=this.password.trim();
        if(word.length==0)
          this.msgpassword="password can not be null";
        return word >=0;
      }
    }
  }
</script>

<style>
  .signUp{
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
  .signUp_style{
    width: 300px;
  }

</style>


