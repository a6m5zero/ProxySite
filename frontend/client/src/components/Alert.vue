<template>
    <div>
        <b-alert variant="danger" show>{{ message }}</b-alert>
    </div>
</template>

<script>
export default {
  props: ['message'],
};
</script>
