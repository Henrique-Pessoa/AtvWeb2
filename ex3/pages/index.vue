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
const isClicked:any = ref(false);

const addWishlist = (item:any) => {
    wishlist.value.push(item);
    isClicked.value = true;
    setTimeout(() => {
        isClicked.value = false;
    }, 1000);
}
</script>

<template>
    <main class="bg-neutral-800 w-screen h-screen">
      <nav class="w-screen h-16  bg-slate-400 border-b-4 border-black justify-end flex items-center text-end">
        <h2 :class="{ 'text-green-400 scale-110 ease-in-out': isClicked, 'text-white': !isClicked, ' text-3xl': isClicked }" class="text-2xl mt-2 mr-2">{{ wishlist.length }}</h2>
        <NuxtLink to="/cart">
        <Icon :class="{ 'text-green-400 ease-in-out': isClicked, '': !isClicked, 'text-3xl text-white': isClicked }" name="uil:cart" class="text-5xl text-white cursor-pointer hover:scale-150 mr-5"/>      </NuxtLink>
      </nav>
      <div class="flex flex-wrap w-screen gap-15 justify-center content-center">
        <div v-for="item in itens" :key="item.name" class="w-72 h-40 bg-neutral-900 flex flex-wrap rounded-2xl ml-10 mt-5 flex-col justify-center content-center">
          <Card :name="item.name" :price="item.price" image="legal"/>
          <button @click="addWishlist(item)" class="bg-yellow-400 w-32 h-10 rounded-2xl">Add to cart</button>
        </div>
      </div>
    </main>
  </template>