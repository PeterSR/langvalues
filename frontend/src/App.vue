<template>
  <div id="app">
    <div class="content">
      <Core />
    </div>
    <Footer />
  </div>
</template>

<script>
import Core from './components/Core.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'app',
  components: {
    Core,
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
