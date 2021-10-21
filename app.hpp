#ifndef __TLSFRONT_APP__H
#define __TLSFRONT_APP__H

#include "ev_app.hpp"

#include <stdint.h>
#include <errno.h>
#include <unistd.h>
#include <openssl/ssl.h>
#include <openssl/err.h>
#include <openssl/x509.h>
#include <openssl/pem.h>
#include <iostream>
#include <fstream>
#include<sstream>
#include <queue>
#include <cstring>
#include <string>
#include <thread>
#include <chrono>
#include <map>
#include <random>
#include <inttypes.h>

#include <subprojects/json/single_include/nlohmann/json.hpp>

using json = nlohmann::json;



enum enum_close_type { close_fin=1
                            , close_reset };

enum enum_close_notify { close_notify_no_send=1
                            , close_notify_send
                            ,  close_notify_send_recv};
                           
enum enum_tls_version { sslv3=0
                            , tls1
                            , tls1_1
                            , tls1_2
                            , tls1_3
                            , tls_all};

struct app_stats : public ev_sockstats
{
    static void dump_json_ev_sockstats (json& j, ev_sockstats* stats)
    {
        SET_JSON_EV_SOCKSTATS(j, stats);
    }

    virtual void dump_json (json& j)
    {
        dump_json_ev_sockstats (j, this);
    };

};

class app : public ev_app
{
public:
    app()
    {
        
    }

    virtual ~app()
    {
    }

    virtual void run_iter(bool tick_sec)
    {
        ev_app::run_iter (tick_sec);
    }

    static void RunLoop(std::vector<app*> *app_list
                        , std::vector<app_stats*> *stats_list);
};

#endif