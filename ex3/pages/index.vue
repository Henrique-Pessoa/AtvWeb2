<script setup lang="ts">
import { ref } from 'vue';
const itens = [
  { name: "Produto 1", price: 50.00 },
  { name: "Produto 2", price: 30.00 },
  { name: "Produto 3", price: 70.00 },
  { name: "Produto 4", price: 45.00 },
  { name: "Produto 5", price: 80.00 },
  { name: "Produto 6", price: 25.00 },
  { name: "Produto 7", price: 55.00 },
  { name: "Produto 8", price: 90.00 },
  { name: "Produto 9", price: 40.00 },
  { name: "Produto 10", price: 65.00 },
  { name: "Produto 11", price: 20.00 },
  { name: "Produto 12", price: 75.00 },
  { name: "Produto 13", price: 35.00 },
  { name: "Produto 14", price: 60.00 },
  { name: "Produto 15", price: 85.00 },
  { name: "Produto 16", price: 55.00 },
  { name: "Produto 17", price: 25.00 },
  { name: "Produto 18", price: 45.00 },
  { name: "Produto 19", price: 70.00 },
  { name: "Produto 20", price: 30.00 },
];
const wishlist:any = ref([]);
const addWishlist = () => {
    wishlist.push(1)
}
</script>


<template>
<main class="bg-neutral-700 w-screen h-screen">
    <nav class="w-screen h-12 bg-zinc-500 justify-end flex">
        <Icon name="uil:cart" class="text-5xl"/>
    </nav>
    <div class="flex flex-wrap w-screen gap-15 justify-center content-center">
        <div v-for="item in itens" class="w-72 h-40 bg-neutral-900 flex flex-wrap rounded-2xl ml-10 mt-5 flex-col justify-center content-center">
        <Card :name="item.name" :price="item.price" image="legal"/>
        <button @click="addWishlist" class="bg-yellow-400 w-32 h-10 rounded-2xl">Add to card</button>
            {{ wishlist }}
    </div>
    </div>
</main>
</template>