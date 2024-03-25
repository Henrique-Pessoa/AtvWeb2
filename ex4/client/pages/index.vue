<script setup lang="ts">
import { ref } from 'vue';
interface Product {
    id:number;
    name: string;
    price: number;
    image: string;
    quantity: number; 
}

const { data: items }: any = await useFetch("http://127.0.0.1:8000/Products/");

const wishlist: Ref<Product[]> = ref([]);

const isClicked: Ref<boolean> = ref(false);

const addWishlist = (item: Product) => {
    const existingItem = wishlist.value.find(p => p.name === item.name);
    if (existingItem) {
        existingItem.quantity++; 
    } else {
        item.quantity = 1; 
        wishlist.value.push(item);
    }
    isClicked.value = true;
    setTimeout(() => {
        isClicked.value = false;
    }, 500);
}

const goToCart = () => {
    const wishlistData = wishlist.value.map(item => ({ id:item.id,name: item.name, price: item.price, quantity: item.quantity, image: item.image }));
    localStorage.setItem('wishlist', JSON.stringify(wishlistData));
}
</script>

<template>
    <main class="bg-neutral-800 w-screen h-screen">
        <nav class="w-screen h-16  bg-slate-400 border-b-4 border-black justify-end flex items-center text-end">
            <h2 :class="{ 'text-yellow-200 scale-150 ease-in-out font-bold': isClicked, 'font-bold': !isClicked}" class="text-2xl mt-2 mr-2">{{ wishlist.reduce((acc, item) => acc + item.quantity, 0) }}</h2>
            <NuxtLink to="/cart" @click="goToCart">
                <Icon :class="{ 'text-yellow-200 scale-125 ease-in-out': isClicked, 'font-bold': !isClicked }" name="uil:cart" class="text-5xl cursor-pointer hover:scale-110 mr-2"/>
            </NuxtLink>
        </nav>
        <div class="flex flex-wrap w-screen gap-15 justify-center content-center">
            <div v-for="item in items" :key="item.name" class="w-72 h-44 bg-neutral-900 flex flex-wrap rounded-2xl ml-10 mt-5 flex-col items-center ">
                <Card :name="item.name" :price="item.price" :image="item.image"/>
                <button @click="addWishlist(item)" class="bg-yellow-400 w-32 h-10 rounded-2xl">Add to cart</button>
            
            </div>
        </div>
    </main>
</template>
