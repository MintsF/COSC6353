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

        <el-form-item label="Password"  :label-width="formLabelWidth">
          <el-col :span="8" style="text-align: left">
            <a @click="showdialog" style="text-align: left;color: blue">change password</a>
            <dialog-bar :show="show" :title="title" @hideModal="hideModal" @submit="submit">
              <div style="text-align: left;">
                <el-form-item label="old password"  label-width="200px" >
                  <el-input placeholder="********" v-model="userlist.oldPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="new password"  label-width="200px">
                  <el-input placeholder="********" v-model="userlist.newPassword" show-password   ></el-input>
                </el-form-item>

                <el-form-item label="confirm password"  label-width="200px">
                  <el-input placeholder="********" v-model="userlist.confirmPassword" show-password   ></el-input>
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
        userlist: {
          userid: '',
          username: '',
          address1: '',
          address2: '',
          city: '',
          state: '',
          zipcode: '',
          oldPassword: '',
          newPassword: '',
          confirmPassword: '',
        },//用户信息表单
        formLabelWidth: "150px",
        columeTypeArr:[{
              value: "AL",
              label: "AL"
          },
          {
              value: "AK",
              label: "AK"
          },
          {
              value: "AS",
              label: "AS"
          },
          {
              value: "AZ",
              label: "AZ"
          },
          {
              value: "AR",
              label: "AR"
          },
          {
              value: "CA",
              label: "CA"
          },
          {
              value: "CO",
              label: "CO"
          },
          {
              value: "CT",
              label: "CT"
          },
          {
              value: "DE",
              label: "DE"
          },
          {
              value: "DC",
              label: "DC"
          },
          {
              value: "FM",
              label: "FM"
          },
          {
              value: "FL",
              label: "FL"
          },
          {
              value: "GA",
              label: "GA"
          },
          {
              value: "GU",
              label: "GU"
          },
          {
              value: "HI",
              label: "HI"
          },
          {
              value: "ID",
              label: "ID"
          },
          {
              value: "IL",
              label: "IL"
          },
          {
              value: "IN",
              label: "IN"
          },
          {
              value: "IA",
              label: "IA"
          },
          {
              value: "KS",
              label: "KS"
          },
          {
              value: "KY",
              label: "KY"
          },
          {
              value: "LA",
              label: "LA"
          },
          {
              value: "ME",
              label: "ME"
          },
          {
              value: "MH",
              label: "MH"
          },
          {
              value: "M",
              label: "MD"
          },
          {
              value: "MA",
              label: "MA"
          },
          {
              value: "MI",
              label: "MI"
          },
          {
              value: "MN",
              label: "MN"
          },
          {
              value: "MS",
              label: "MS"
          },
          {
              value: "MO",
              label: "MO"
          },
          {
              value: "MT",
              label: "MT"
          },
          {
              value: "NE",
              label: "NE"
          },
          {
              value: "NV",
              label: "NV"
          },
          {
              value: "NH",
              label: "NH"
          },
          {
              value: "NJ",
              label: "NJ"
          },
          {
              value: "NM",
              label: "NM"
          },
          {
              value: "NY",
              label: "NY"
          },
          {
              value: "NC",
              label: "NC"
          },
          {
              value: "ND",
              label: "ND"
          },
          {
              value: "MP",
              label: "MP"
          },
          {
              value: "OH",
              label: "OH"
          },
          {
              value: "OK",
              label: "OK"
          },
          {
              value: "OR",
              label: "OR"
          },
          {
              value: "PW",
              label: "PW"
          },
          {
              value: "PA",
              label: "PA"
          },
          {
              value: "PR",
              label: "PR"
          },
          {
              value: "RI",
              label: "RI"
          },
          {
              value: "SC",
              label: "SC"
          },
          {
              value: "SD",
              label: "SD"
          },
          {
              value: "TN",
              label: "TN"
          },
          {
              value: "TX",
              label: "TX"
          },
          {
              value: "UT",
              label: "UT"
          },
          {
              value: "VT",
              label: "VT"
          },
          {
              value: "VI",
              label: "VI"
          },
          {
              value: "VA",
              label: "VA"
          },
          {
              value: "WA",
              label: "WA"
          },
          {
              value: "WV",
              label: "WV"
          },
          {
              value: "WI",
              label: "WI"
          },
          {
              value: "WY",
              label: "WY"
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
         }],

        }
        }
    },
    created: function(){
      var that= this;
      that.userlist.userid=localStorage.getItem('username');
      var postData = this.$qs.stringify({
      userid: that.userlist.userid,
      // username: that.userlist.username,
      // address1: that.userlist.address1,
      // address2: that.userlist.address2,
      // city: that.userlist.city,
      // state: that.userlist.state,
      // zipcode: that.userlist.zipcode,
      });
      this.$axios.post('/api/initProfile/',postData).then(res=>{
        console.log(res.data);
        that.userlist.userid=eval(res.data.userid);
        that.userlist.username=res.data.username;
        that.userlist.address1=res.data.address1;
        that.userlist.address2=res.data.address2;
        that.userlist.city=res.data.city;
        that.userlist.state=res.data.state;
        that.userlist.zipcode=res.data.zipcode;
      }).catch((err)=>{
        console.log("can not connec to server")
      })


    },

    methods:{
        hideModal() {
            // 取消弹窗回调
            this.oldPassword='';
            this.newPassword='';
            this.confirmPassword='';
            this.show = false
        },

        submit() {
            // 确认弹窗回调
            
            var userInfo = localStorage.getItem('username');

            this.userlist.userid=userInfo;
             console.log(userInfo)
            if(this.userlist.oldPassword==''){
              alert("please input the old password")
              return false;
            }
            if (this.userlist.newPassword==''||this.userlist.confirmPassword==''){
              alert("new password and confirmPassword can not be none");
              return false;
            }

            if(this.userlist.newPassword!=this.userlist.confirmPassword){
              alert("password do not match")
              return false;
            }

            var postData =this.$qs.stringify ({
              username: userInfo,
                // oldpassword: this.userlist.password,
              password: this.userlist.oldPassword,
              newPassword: this.userlist.newPassword,
            });
            this.$axios.post('/api/changepassword/',postData).then(res=>{
              console.log("connect to the server success");
              console.log(res.data);
              if (res.data.code==4001){
                alert(res.data.msg)
              }
              if (res.data.code==4002){
                console.log(res.data.msg)
                this.show = false

              }
              

              }).catch((err)=>{
                console.log("can not connect to the server")
              })
            


        },
        showdialog(){
          this.show=true
        },
        BacktoHome(){
          this.$router.push('/FuelQuote')

        },
        EditorUserClick(formName){
          var that= this;
          that.userlist.userid = localStorage.getItem('username');
          console.log(that.userlist.address1)
          if(that.userlist.username==''||that.userlist.username.length>50){
            alert("full name can not be none or no more than 50 characters");
            return false;
          }

          if(that.userlist.address1==''){
            alert("address1 can not be none or no more than 100 characters");
            return false;
          }

          if(that.userlist.city==''){
            alert("please enter your city");
            return false;
          }
          if (that.userlist.state==''){
            alert("please enter your state");
            return false;
          }
          console.log(that.userlist.zipcode.length);
          let value = that.userlist.zipcode.replace('/(^\s*)|(\s*$)','');
          let num = Number(value);
          if(that.userlist.zipcode.length<5|| that.userlist.zipcode.length>9||isNaN(num)){
            alert("please enter at least 5 digits of zipcode and no more than 9 digits");
            return false;
          }
         

          var postData = this.$qs.stringify({
            userid: that.userlist.userid,
            username: that.userlist.username,
            address1: that.userlist.address1,
            address2: that.userlist.address2,
            city: that.userlist.city,
            state: that.userlist.state,
            zipcode: that.userlist.zipcode,
          });
          this.$axios.post('/api/profile/',postData).then(res=>{
            console.log(res.data)
            if(res.data.code==3001){
              alert(res.data.msg)
            }else if (res.data.code==3002){
              alert(res.data.msg)
            }
          }).catch((err)=>{
            console.log("can not connec to server")
          })

          

        }

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