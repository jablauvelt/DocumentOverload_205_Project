(ns wordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn wordcount [options]
   [
    ;; spout configuration
    {"kafka-spout" (python-spout-spec
          options
          "spouts.kafka_storm_geopy_spout.KafkaSpout"
          ["message"]
          )
    }
    ;; bolt configuration
    {"geopy-bolt" (python-bolt-spec
          options
          {"kafka-spout" :shuffle}
          "bolts.kafka_storm_geopy_bolt.GeopyBolt"
          ["filename" "zipcode"]
          :p 1
          )
    }
  ]
)
