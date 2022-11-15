const axios = require("axios").default;

const axios_post = (target_url, data) => {
  //let res = 'r';
  return axios({
    method: "post",
    url: target_url,
    headers: {
      "Content-Type": "application/json",
    },
    data: data,
  })
    .then((response) => {
      console.log(response.data);
    })
    .catch((error) => {
      console.log(error.response.data);
    });
};
const axios_get = async (target_url) => {
  try {
    const { data: response } = await axios.get(target_url);
    return response;
  } catch (error) {
    console.log(error.response.data);
  }
};

const ngrok_url = axios_get("http://localhost:4040/api/tunnels").then(
  (response) => response["tunnels"][0]?.public_url
);

const update_webhook = async (server_url, subpath = "") => {
  /*Use this on target machine(client) to send the current url where all webhhooks should be forwarded to
    Args:
        server_url:str= The base address of where the webhook forwarder is hosted (the permanent url of the hosted server
                        i.e: https://herokuapp.xyzapp.app)to*/
  const webhook_url = await ngrok_url;
  const payload = JSON.stringify({
    webhook_url: webhook_url + "/" + subpath.replace(/^\/|\/$/g, ""),
  });
  const _url = `${server_url.trim().replace(/\/$/g, "")}/setwebhook`;
  return axios_post((target_url = _url), (data = payload));
};

module.exports = update_webhook;
