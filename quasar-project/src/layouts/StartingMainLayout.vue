<template>
  <q-layout view="lHh Lpr lFf">
  <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent, ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'
export default {
  name: 'StartingMainLayout',
  
}

</script>
