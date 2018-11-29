from datadog import initialize, api

options = {
    'api_key': 'd554d99611a2acc7ae655efc22d2ceae',
    'app_key': '1f08505a862908afd99479cefad7c967166fc0a3'
}

initialize(**options)

title = "Visualizing Data (Timeboard)"
description = "created by anders.iderstrom@gmail.com via API"
graphs = [{
"definition": {
          "status": "done",
          "viz": "timeseries",
          "requests": [
            {
              "q": "avg:my_custom_agent_check_metric.random{host:ubuntu-1804-ec2}",
              "aggregator": "avg",
              "style": {
                "width": "normal",
                "palette": "dog_classic",
                "type": "solid"
              },
              "type": "line",
              "conditional_formats": []
            }
          ],
          "autoscale": "true"
        },
        "title": "my_custom_agent_check_metric.random scoped over docker host"
      }]

template_variables = [{
    "name": "host1",
    "prefix": "host",
    "default": "host:my-host"
}]

read_only = True
api.Timeboard.create(title=title,
                     description=description,
                     graphs=graphs,
                     template_variables=template_variables,
                     read_only=read_only)
