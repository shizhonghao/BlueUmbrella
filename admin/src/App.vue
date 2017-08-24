<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app',
  created(){
    this.$ajax.get('/login')
    .then((response) => {
      sessionStorage.setItem("state", response.data.LoggedIn)
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
</style>
