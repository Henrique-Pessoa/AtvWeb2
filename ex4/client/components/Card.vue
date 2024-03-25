<script setup lang="ts">
import { ref, defineProps } from 'vue';

const itens = defineProps({
    name:String,
    image:String,
    price:Number,
});
</script>

<template>
  <div class="flex flex-col">
    <h1 class=" text-yellow-500 font-bold ">{{ itens.name }}</h1>
    <img :src="image" class="w-20 "/>
    <h3 class="text-white font-medium ml-2">R${{itens.price}}</h3>
  </div>
</template>
