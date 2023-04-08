<script setup>
    const props = defineProps(['movie'])
</script>

<template>
    <div class="card mb-3">
        <div class="row no-gutters">
        <div class="col-md-4">
            <img v-bind:src="movie.poster" class="card-img">
        </div>
        <div class="col-md-8">
            <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">{{ movie.description }}</p>
            </div>
        </div>
        </div>
    </div>
</template>

<style scoped>
    div.card {
        margin-right: 5rem;
        padding-left: 0;
        width: 500px;
    }
    .card-text {
        font-size: small;
    }
</style>
