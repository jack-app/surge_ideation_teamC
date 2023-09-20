<template>
  <div class="signup-view">
    <SignupForm :setup=handleSignup />
  </div>
</template>

<script>
  import { defineComponent } from 'vue';
  import SignupForm from '@/components/molecules/SignupForm.vue';

  export default defineComponent({
    name: 'SignupView',
    components: {
        SignupForm
    },
    methods: {
        handleSignup(authInfo) {
            console.log(authInfo)
            return this.$store.dispatch('signup', authInfo)
        }
    }
  })
</script>


<style scoped>
.signup-view {
  width: 400px;
  margin: auto;
}
</style>