<template>
<div>
  <div style="position:relative;">
    <img height="auto" width="auto" src="@/assets/accounts_card.jpg">
    <logo></logo>
    <form-button></form-button>
  </div>



  <div id="img-position">
    <img width="110"  height="auto" src="@/assets/노리개.png">
  </div>  
</div>
</template>




<script scoped>
import Logo from '@/components/signup/Logo'
import FormButton from '@/components/signup/FormButton'

export default {
  name:'Card',
  components: {
    Logo,
    FormButton
  }
}
</script>

<style scoped>
#img-position{
  display: flex;
  justify-content: center;
}


</style>