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
import Logo from '@/components/login/Logo'
import FormButton from '@/components/login/FormButton'

export default {
  name:'Card',
  components: {
    Logo,
    FormButton
  }
}
</script>

<style>
#img-position{
  display: flex;
  justify-content: center;
}


</style>