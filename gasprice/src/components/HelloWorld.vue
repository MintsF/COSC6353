<template>
  <div>
    <div class="main-container">
      <h2 >Profile</h2>
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
         <el-col :span="8">  
         <el-select v-model="userlist.state" placeholder="Please select one ">
           <el-option v-for="(item,index) in columeTypeArr" :key="index" :label="item.label" :value="item.value">
           </el-option>
         </el-select>

         </el-col>
        </el-form-item>


        <el-form-item label="ZipCode" prop="zipcode" :label-width="formLabelWidth">
         <el-col :span="21">  <el-input v-model="userlist.zipcode" placeholder="Please enter Zipcode"></el-input></el-col>
        </el-form-item>

        <el-form-item label="Password" prop="password" :label-width="formLabelWidth">
          <el-col :span="8" style="text-align: left">
            <a @click="showdialog" style="text-align: left;color: blue">change password</a>
            <dialog-bar :show="show" :title="title" @hideModal="hideModal" @submit="submit">
              <div style="text-align: left">
                <el-form-item label="old password" label-width="200px" >
                  <el-input placeholder="********" v-model="userlist.userPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="new password" label-width="200px">
                  <el-input placeholder="********" v-model="userlist.userPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="confirm password" label-width="200px">
                  <el-input placeholder="********" v-model="userlist.userPassword" show-password   ></el-input>
                </el-form-item>
              </div>


            </dialog-bar>

          </el-col>
        </el-form-item>

        <el-form-item >
         <el-col :span="8" style="text-align: left"> 
          <el-button type="primary" @click="BacktoHome" style="text-align: left" >Back</el-button></el-col>
        <el-col :span="8" style="text-align: left">
          <el-button type="primary" @click="EditorUserClick('userlist')" style="text-align: right">Save</el-button></el-col>

        </el-form-item>

      </el-form>
    </div>

 
  </div>
  
</template>

<script >
  import dialogBar from './dialog.vue'

  export default{
       components:{
        'dialog-bar': dialogBar,
    },
    data(){
        return{
        title: 'Change password',
        show: false,
        userlist: {},//用户信息表单
        formLabelWidth: "150px",
        columeTypeArr:[{
            value:'String',
            label:'CA'
        },{
            value:'String',
            label:'WA',
        },{
            value:'String',
            label:'NY'
        },{
            value:'String',
            label:'TX'
        }],

        rules: {
        username: [{
          required: true,
          message: "please enter your name"
        }],
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
         }]
        }
        }
    },
    methods:{
        hideModal() {
            // 取消弹窗回调
            this.show = false
        },

        submit() {
            // 确认弹窗回调
            this.show = false
        },
        showdialog(){
          this.show=true
        },
        BacktoHome(){
          this.$router.push('/FuelQuote')

        },

    }
  }
  
</script>

<style type="text/css">

  .el-button--primary{
    font-family: "Roboto", sans-serif;
    font-weight: 600;
    background:linear-gradient(150deg,  #97c74e 0%, #2ab9a5 100%);
  }
</style>