import Vuex from 'vuex'
import Vue from 'vue'

import api from './api.js'

Vue.use(Vuex);

const store = new Vuex.Store({
  /*strict: process.env.NODE_ENV === 'production',*/
  modules: {
    api
  }
})
export default store;
