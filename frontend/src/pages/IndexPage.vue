<template>
  <div class="main__container">
    <div class="empty"></div>
    <div class="action">
      <q-btn class="btn" color="primary" label="Начать" @click="$router.push('/sessions')" />
    </div>
    <div class="info">
      <h1 class="title">ФГБУ "РФИ Минприроды России"</h1>
    </div>
    <div class="float-gallery" >
      <img class="img1" src="../assets/placeholder/1.jpg" alt="">
      <img class="img2" src="../assets/placeholder/2.jpg" alt="">
      <img class="img3" src="../assets/placeholder/3.jpg" alt="">
      <img class="img4" src="../assets/placeholder/4.jpg" alt="">
      <img class="img5" src="../assets/placeholder/5.jpg" alt="">
      <img class="img6" src="../assets/placeholder/6.jpg" alt="">
      <img class="img7" src="../assets/placeholder/7.jpg" alt="">
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue';
</script>

<style scoped lang="scss">
// $
.main__container {
  position: relative;
  height: 100%;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
  z-index: 1000;
}

.empty {
  height: 1px;
}

.action {
  display: flex;
  justify-content: center;
  margin-top:30%;

  .btn {
    margin-top: 60px;
    padding: 10px 20px;
    font-size: 24px;
    border-radius: 5px;
    transition: all .3s;

    &:hover {
      background-color: $teal-7;
    }
  }
}

.info {
  padding-bottom: 50px;
}

.title {
  font-size: 32px;
  font-weight: 500;
}

.subtitle {
  font-size: 24px;
}

.float-gallery {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;

  img {
    position: relative;
    z-index: 1;
    object-fit: cover;
    width: auto;
    height: 60%;
    border-radius: 20px;
  }

  .img1 {
    top: 5%;
    left: 5%;
    animation: circle1 30s linear infinite;
  }

  .img2 {
    top: 30%;
    left: -20%;
    animation: circle2 30s linear infinite;
  }

  .img3 {
    top: -5%;
    left: 30%;
    animation: circle3 30s linear infinite;
  }

  .img4 {
    top: -5%;
    left: 80%;
    animation: circle4 30s linear infinite;
  }

  .img5 {
    top: 70%;
    left: 5%;
    animation: circle5 30s linear infinite;
  }

  .img6 {
    top: 0%;
    left: 65%;
    animation: circle6 30s linear infinite;
  }

  .img7 {
    top: 30%;
    left: 10%;
    animation: circle7 30s linear infinite;
  }
}

@keyframes circle1 {
  from {
    transform: rotate(0deg) translate(-30px) rotate(0deg);
  }

  to {
    transform: rotate(360deg) translate(-30px) rotate(-360deg);
  }
}

@keyframes circle2 {
  from {
    transform: rotate(360deg) translate(-30px) rotate(-360deg);
  }

  to {
    transform: rotate(0deg) translate(-30px) rotate(0deg);
  }
}

@keyframes circle3 {
  from {
    transform: rotate(360deg) translate(-30px) rotate(-360deg);
  }

  to {
    transform: rotate(0deg) translate(-30px) rotate(0deg);
  }
}

@keyframes circle4 {
  from {
    transform: rotate(360deg) translate(-60px) rotate(-360deg);
  }

  to {
    transform: rotate(0deg) translate(-60px) rotate(0deg);
  }
}

@keyframes circle5 {
  from {
    transform: rotate(360deg) translate(-80px) rotate(-360deg);
  }

  to {
    transform: rotate(0deg) translate(-80px) rotate(0deg);
  }
}

@keyframes circle6 {
  from {
    transform: rotate(-360deg) translate(-30px) rotate(360deg);
  }

  to {
    transform: rotate(0deg) translate(-30px) rotate(0deg);
  }
}

@keyframes circle7 {
  from {
    transform: rotate(360deg) translate(-50px) rotate(-360deg);
  }

  to {
    transform: rotate(0deg) translate(-50px) rotate(0deg);
  }
}
</style>
