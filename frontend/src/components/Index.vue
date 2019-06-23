<template>
  <div>Test {{msg}}</div>
</template>

<script>
import axios from 'axios';

axios.get(`/api`).then(data => {
  console.log(data)
});

export default {
  name: 'Test',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>

</style>
