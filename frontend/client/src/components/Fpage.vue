<template>
<div class = "container">
  <h3 class="text-center">Checked and Working SOCKS Proxy</h3>
  <h4 class = "text-center"> Updates every 5 minutes</h4>
  <p class = "text-center">LastUpdate: {{ lastupdate }} </p>
  <alert :message = "message" v-if="showAlert"></alert>
    <div id="filter-line" class="d-flex flex-row align-items-center justify-content-center">
   <b-form-checkbox switch size="lg" class="filter_checkbox"
      id="checkbox-socks5"
      v-model= "socks5_selected"
      name="checkbox-socks5"
      value="accepted"
      unchecked-value="not_accepted"
      @input = "filterTable"
    >
    SOCKS 5
    </b-form-checkbox>
       <b-form-checkbox switch size="lg" class="filter_checkbox"
      id="checkbox-socks4"
      v-model= "socks4_selected"
      name="checkbox-socks4"
      value="accepted"
      unchecked-value="not_accepted"
      @input = "filterTable"
    >
    SOCKS 4
    </b-form-checkbox>
    <b-button size="sm" id="download_button" @click="fileDownload">
      Download .txt (IP:PORT)</b-button>
    </div>
  <b-table ref="table" striped hover :items="items"></b-table>
</div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

let filterURL = '';
let downloadURL = '';
const proxyURL = 'http://127.0.0.1/api/get_proxy/';
const timeURL = 'http://127.0.0.1/api/update_time/';

export default {
  components: { Alert },

  name: 'Fpage',
  data() {
    return {
      socks5_selected: ['accepted'],
      socks4_selected: ['accepted'],
      lastupdate: [],
      items: [],
      message: '',
      showAlert: false,
    };
  },
  props: {
    msg: String,
  },
  methods: {
    getProxy() {
      axios.get(proxyURL)
        .then((response) => {
          this.items = response.data;
        });
      axios.get(timeURL)
        .then((response) => {
          console.log(response);
          this.lastupdate = response.data[0].date;
          console.log(this.lastupdate);
        });
    },
    filterTable() {
      this.showAlert = false;
      console.log(this.socks5_selected);
      if (this.socks5_selected[0] === 'accepted' && this.socks4_selected[0] === 'accepted') {
        filterURL = `${proxyURL}`;
        axios.get(filterURL)
          .then((response) => {
            console.log(response);
            this.items = response.data;
          });
      } else if (this.socks5_selected[0] === 'accepted') {
        filterURL = `${proxyURL}?type=socks5`;
        axios.get(filterURL)
          .then((response) => {
            console.log(response);
            this.items = response.data;
          });
      } else if (this.socks4_selected[0] === 'accepted') {
        filterURL = `${proxyURL}?type=socks4`;
        axios.get(filterURL)
          .then((response) => {
            console.log(response);
            this.items = response.data;
          });
      } else {
        this.items = [];
      }
      this.$refs.table.refresh();
    },
    fileDownload() {
      if (this.socks5_selected[0] === 'accepted' && this.socks4_selected[0] === 'accepted') {
        downloadURL = 'http://127.0.0.1/api/file_download/';
      } else if (this.socks5_selected[0] === 'accepted' && this.socks4_selected[0] !== 'accepted') {
        downloadURL = 'http://127.0.0.1/api/file_download/?filter=socks5';
      } else if (this.socks5_selected[0] !== 'accepted' && this.socks4_selected[0] === 'accepted') {
        downloadURL = 'http://127.0.0.1/api/file_download/?filter=socks4';
      } else {
        this.message = 'Push checkbox Filter';
        this.showAlert = true;
        return;
      }
      axios.get(downloadURL, {
        responseType: 'blob',
      }).then((response) => {
        console.log(response.data);
        const blob = new Blob([response.data], { type: 'text/plain' });
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = `${this.lastupdate}.txt`;
        link.click();
      });
    },
  },
  created() {
    this.getProxy();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
h4 {
  margin: 5px 0 5px;
}
a {
  color: #42b983;
}
.filter_checkbox {
  margin-left: 20px;
}
#download_button {
  /* margin-bottom: 20px; */
  margin-left: 20px;
}
#filter-line {
  margin-bottom: 20px;
}
</style>
