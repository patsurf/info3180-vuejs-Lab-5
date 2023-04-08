<script setup>
    import { ref, onMounted } from 'vue';
    import Card from '../components/Card.vue';
    let movies = ref([]);
    function fetchMovies(){
        fetch("/api/v1/movies", {
            method: 'GET',
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            movies.value = data.movies;
        })
        .catch(function (error) {
            console.log(error);
        });
    }
    onMounted(() => {
        fetchMovies();
    });
</script>

<template>
    <main class="container py-5">
        <h1 class="display-5 mb-3">Movies</h1>
        <div class="row row-cols-1 row-cols-md-4 g-4">
            <Card v-bind:movie="movie" v-for="movie in movies" :key="movie.id" />
        </div>
    </main>
</template>
