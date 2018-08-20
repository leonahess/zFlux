from influx_pusher import InfluxPusher


class PerformanceInfluxPusher(InfluxPusher):

    def assembleJsonBody(self, cycle_stats):
        """assembles a valid json construct for pushing the killmail to the database"""
        json_body = [{"measurement": "performance",
                "tags": {
                },
                "fields": {
                    "#cycles": 1,
                    "cycle_time": cycle_stats.cur_cycle,
                    "shortest_cycle": cycle_stats.shortest_cycle,
                    "longest_cycle": cycle_stats.longest_cycle,
                    "avg100": cycle_stats.avg_last100_cycle,
                    "avg1000": cycle_stats.avg_last1000_cycle,
                    "counter": cycle_stats.counter
                },
                "time": cycle_stats.cycle_start,
                "time_precision": "s"
        }]

        return json_body

    def writeToDatabase(self, cycle_stats):
        """pushes the json construct to the database"""
        json = self.assembleJsonBody(cycle_stats)

        self.client.write_points(json, protocol="json")
