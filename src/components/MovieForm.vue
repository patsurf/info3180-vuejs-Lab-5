<script setup>
    import { ref, onMounted } from "vue";
    let csrf_token = ref("");
    function getCsrfToken() {
        fetch('/api/v1/csrf-token')
        .then((response) => response.json())
        .then((data) => {
            console.log(data);
            csrf_token.value = data.csrf_token;
        })
    }
    function saveMovie(){
        let movieForm = document.getElementById('movieForm');
        let form_data = new FormData(movieForm);
        fetch("/api/v1/movies", {
            method: 'POST',
            body: form_data,
            headers: {
                'X-CSRFToken': csrf_token.value
            }
        })
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            console.log(data);
        })
        .catch(function (error) {
            console.log(error);
        });
    }
    onMounted(() => {
        getCsrfToken();
    });
</script>

<template>
    <div class="form-container">
    <h2>Upload Form</h2>
    <form @submit.prevent="saveMovie" enctype="multipart/form-data" id="movieForm">
        <div class="form-group mb-3">
        <label for="title" class="form-label">Movie Title</label>
        <input type="text" name="title" class="form-control" />
        </div>
        <div class="form-group mb-3">
        <label for="description" class="form-label">Description</label>
        <textarea name="description" class="form-control" rows="3"></textarea>
        </div>
        <div class="form-group mb-3">
        <label for="poster" class="form-label">Poster</label>
        <input type="file" name="poster" class="form-control" />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
    </form>
    </div>
</template>

<style scoped>
    div.form-container {
        width: auto;
        margin-left: 50px;
        margin-right: 50px;
    }
</style>
