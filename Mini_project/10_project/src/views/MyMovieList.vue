<template>
<div style="margin-top: 7%;">
    <h1 class="mb-3" id="center">나의 영화목록</h1>
    <div style="margin-left: 33.3%;" class="d-flex justify-content-center col-4">
      <div class="input-group mb-3">
        <input type="text" class="form-control" placeholder="어떤 영화가 보고 싶나요? :)" v-model="inputMovie" @keyup.enter="createMyMovie">
        <button class="btn btn-outline-secondary" type="button" id="button-addon2" @click="createMyMovie">Enter</button>
      </div>
    </div>
    <div class="d-flex justify-content-center">
      <div class="col-4 ">
        <MyList/>
        <div class=" d-flex justify-content-end">
          <!-- <div class="btn btn-success btn-sm mt-2" @click="deleteDone">완료목록 지우기</div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MyList from '@/components/MyList'

export default {
  name: 'MyMovieList',
  data: function () {
    return {
      inputMovie: '',
    }
  },
  components: {
    MyList,
  },
  methods: {
    createMyMovie: function () {
      const movieItem = {
        title: this.inputMovie,
        completed: false,
      }
      this.$store.dispatch('createMyMovie', movieItem)
      this.inputMovie = ''
    }
  }
}
</script>

<style>

</style>