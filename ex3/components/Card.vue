<script setup lang="ts">
import { ref, defineProps } from 'vue';

const itens = defineProps({
    name:String,
    image:String,
    price:Number,
});
</script>

<template>
  <div class=" flex-wrap rounded-2xl">
    <h1 class=" text-yellow-500 font-bold ml-5">{{ itens.name }}</h1>
    <img/>
    <h3 class="text-white font-medium ml-5">{{itens.price}}</h3>
  </div>
</template>
