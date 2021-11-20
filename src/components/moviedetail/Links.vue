<template>
  <div>
    <v-breadcrumbs
      :items="items"
      divider="\"
    ></v-breadcrumbs>


  </div>
</template>

<script>
export default {
  name:'Links',
  data: () => ({
      items: [
        {
          text: 'DETAIL',
          disabled: false,
          href: '1',
        },
        {
          text: 'trailer',
          disabled: false,
          href: '1',
        },
        {
          text: 'review',
          disabled: false,
          href: '1',
        },
      ],
    }),
}
</script>

<style>

</style>