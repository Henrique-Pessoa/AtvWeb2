<script setup lang="ts">
import { ref } from 'vue';
const wishlist = ref()
onMounted( () => {
    wishlist.value = localStorage.getItem('wishlist')
})
</script>

<template>
  <div>
    <h1>Carrinho</h1>
    <ul>
     {{ wishlist }}
    </ul>
  </div>
</template>
