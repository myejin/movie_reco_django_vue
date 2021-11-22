<template>
  <div>
    {{ from }} : {{ content }} ({{ datetime }})
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    data: String,
  },
  data: function () {
    return {
      from: '',
      content: '',
      datetime: '',
    }
  },
  created: function () {
    const tmp = this.data.split('\n')
    this.from = tmp[0]
    this.content = tmp[1]
    this.datetime = tmp[2]
  }
}
</script>

<style>
</style>