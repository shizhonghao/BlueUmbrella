<template>
  <div id="app">
    <!-- <transition name="fade"> -->
      <router-view></router-view>
    <!-- </transition> -->
  </div>
</template>

<script>
export default {
  name: 'app',
  data(){
    return {
      status: false
    }
  },
  created(){
    this.$ajax.get('/login')
    .then((response) => {
      console.log(response.data)
      sessionStorage.setItem("state", response.data.LoggedIn)
      sessionStorage.setItem("username", response.data.CurrentUser)
      if(JSON.parse(sessionStorage.getItem("state"))){
        this.$router.push('/view')
      } else {
        this.$router.push('/login')
      }
    })
    .catch((error) => {
      console.log(error)
    })
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

/* .fade-enter-active, .fade-leave-active {
  transition: opacity .5s
}
.fade-enter, .fade-leave-active {
  opacity: 0
}
.slide-enter-active {
  transition: all .3s ease;
}
.slide-leave-active {
   transition: all .3s cubic-bezier(1.0, 0.5, 0.8, 1.0); 
}
.slide-enter, .slide-leave-active {
  transform: translateX(10px);
  opacity: 0;
}   */
</style>
