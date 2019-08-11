<template>
  <div id="app">
    <div class="content">
        <Test />
    </div>
    <Footer />
  </div>
</template>

<script>
import Test from './components/Test.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'app',
  components: {
    Test,
    Footer
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  height: 100%;
  display: flex;
  flex-direction: column;
}

.content {
  flex: 1 0 auto;

  padding: 1em;
}
</style>
