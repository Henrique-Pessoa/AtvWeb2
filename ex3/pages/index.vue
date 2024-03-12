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

const wishlist:Ref<{ name: string; price: number }[]> = ref([]);
const isClicked:Ref<boolean> = ref(false);

const addWishlist = (item: { name: string, price: number }) => {
    wishlist.value.push(item);
    isClicked.value = true;
    setTimeout(() => {
        isClicked.value = false;
    }, 500);
}
const goToCar = () => {
  const wishlistData = wishlist.value.map((item: { name: string; price: number }) => ({ name: item.name, price: item.price }));
  localStorage.setItem('wishlist', JSON.stringify(wishlistData));
}
</script>

<template>
    <main class="bg-neutral-800 w-screen h-screen">
      <nav class="w-screen h-16  bg-slate-400 border-b-4 border-black justify-end flex items-center text-end">
        <h2 :class="{ 'text-yellow-200 scale-150 ease-in-out font-bold': isClicked, 'font-bold': !isClicked}" class="text-2xl mt-2 mr-2">{{ wishlist.length }}</h2>
        <NuxtLink to="/cart" @click="goToCar">
        <Icon :class="{ 'text-yellow-200 scale-125 ease-in-out': isClicked, 'font-bold': !isClicked}" name="uil:cart" class="text-5xl cursor-pointer hover:scale-110 mr-5"/>      </NuxtLink>
      </nav>
      <div class="flex flex-wrap w-screen gap-15 justify-center content-center">
        <div v-for="item in itens" :key="item.name" class="w-72 h-40 bg-neutral-900 flex flex-wrap rounded-2xl ml-10 mt-5 flex-col justify-center content-center">
          <Card :name="item.name" :price="item.price" image="legal"/>
          <button @click="addWishlist(item)" class="bg-yellow-400 w-32 h-10 rounded-2xl">Add to cart</button>
        </div>
      </div>
    </main>
  </template>